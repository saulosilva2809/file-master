from . import views

from django.urls import path


urlpatterns = [
    path('list_positions_room/<int:room_pk>/', views.list_positions_room, name='list_positions_room'),
    path('add_position_room/<int:room_pk>/', views.add_position_room, name='add_position_room'),
    path('edit_position_room/position/<int:position_pk>/room/<int:room_pk>/', views.edit_position_room, name='edit_position_room'),
    path('delete_position_room/position/<int:position_pk>/room/<int:room_pk>/', views.delete_position_room, name='delete_position_room'),
    path('set_position_from_user/room/<int:room_pk>/user/<int:user_pk>/', views.set_position_from_user, name='set_position_from_user'),
    path('remove_positions_from_user/room/<int:room_pk>/user/<int:user_pk>/', views.remove_positions_from_user, name='remove_positions_from_user'),
]
