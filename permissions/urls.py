from . import views

from django.urls import path


urlpatterns = [
    path('list/<int:room_pk>/', views.list_perms_room, name='list_perms_room'),
    path('add_perms_from_user/room/<int:room_pk>/user/<int:user_pk>/', views.add_perms_from_user, name='add_perms_from_user'),
    path('remove_perms_from_user/room/<int:room_pk>/user/<int:user_pk>/', views.remove_perms_from_user, name='remove_perms_from_user'),
]
