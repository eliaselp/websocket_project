import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Room
from django.contrib.auth.decorators import login_required

@login_required
def room_list(request):
    rooms = Room.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'rooms/index.html', {'rooms': rooms})


@login_required
@csrf_exempt
def create_room(request):
    # Eliminamos @require_http_methods temporalmente
    print("="*50)
    print("METHOD:", request.method)
    print("BODY:", request.body)
    print("HEADERS:", dict(request.headers))
    print("="*50)
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        # Intentamos parsear el JSON
        data = json.loads(request.body)
        room_name = data.get('name')
        
        if not room_name:
            return JsonResponse({'error': 'Room name is required'}, status=400)
            
        # Creamos la sala
        room = Room.objects.create(name=room_name)
        
        return JsonResponse({
            'success': True,
            'name': room.name,
            'master_token': room.master_token,
            'slave_token': room.slave_token,
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_room(request, room_name):
    try:
        room = Room.objects.get(name=room_name, is_active=True)
        room.is_active = False
        room.save()
        return JsonResponse({'message': 'Room deleted successfully'})
    except Room.DoesNotExist:
        return JsonResponse({'error': 'Room not found'}, status=404)