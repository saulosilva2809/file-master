from . import views
from django.urls import path

urlpatterns = [
    path(
        'create_room_password_access/', 
        views.create_room_password_access, 
        name='create_room_password_access'
    ),
    path('create_room/', views.create_room, name='create_room'),
    path('connect/', views.connect_room, name='connect_room'),
    path('my_rooms/', views.my_rooms, name='my_rooms'),
    path('room/<int:pk>/', views.room_detail, name='room_detail'),
    path('room/<int:room_pk>/remove_user/<int:user_pk>/', views.remove_user_from_room, name='remove_user_from_room'),
]
