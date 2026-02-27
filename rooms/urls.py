from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('create/', views.create_room, name='create_room'),
    path('delete/<str:room_name>/', views.delete_room, name='delete_room'),
]