import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room

class RoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'room_{self.room_name}'
        self.token = self.scope['url_route']['kwargs']['token']
        
        room = await self.get_room()
        if not room:
            await self.close()
            return
        
        self.room = room
        self.user_type = await self.get_user_type()
        
        if not self.user_type:
            await self.close()
            return
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_connected',
                'user_type': self.user_type,
                'message': f'{self.user_type} connected to room {self.room_name}'
            }
        )
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_disconnected',
                'user_type': self.user_type,
                'message': f'{self.user_type} disconnected from room {self.room_name}'
            }
        )
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json.get('type', 'command')
        
        if message_type == 'command' and self.user_type == 'master':
            command = text_data_json['command']
            
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'send_command',
                    'command': command,
                    'from_master': True
                }
            )
    
    async def send_command(self, event):
        if self.user_type == 'slave':
            await self.send(text_data=json.dumps({
                'type': 'command',
                'command': event['command']
            }))
    
    async def user_connected(self, event):
        await self.send(text_data=json.dumps({
            'type': 'system',
            'message': event['message'],
            'user_type': event['user_type']
        }))
    
    async def user_disconnected(self, event):
        await self.send(text_data=json.dumps({
            'type': 'system',
            'message': event['message'],
            'user_type': event['user_type']
        }))
    
    @database_sync_to_async
    def get_room(self):
        try:
            return Room.objects.get(name=self.room_name, is_active=True)
        except Room.DoesNotExist:
            return None
    
    @database_sync_to_async
    def get_user_type(self):
        if self.token == self.room.master_token:
            return 'master'
        elif self.token == self.room.slave_token:
            return 'slave'
        return None