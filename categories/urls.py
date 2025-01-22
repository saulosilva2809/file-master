from . import views

from django.urls import path


urlpatterns = [
    path(
        'category/room/<int:room_pk>/',
        views.categories_room_detail,
        name='categories_room_detail,'
    ),
    path(
        'category/add/room/<int:room_pk>/',
        views.category_add,
        name='category_add'
    ),
    path(
        'category/<int:category_pk>/edit/room/<int:room_pk>/',
        views.category_edit,
        name='category_edit'
    ),
    path(
        'category/<int:category_pk>/delete/room/<int:room_pk>/',
        views.category_delete,
        name='category_delete'
    ),
]
