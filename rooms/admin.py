from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'master_token', 'slave_token', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name',)