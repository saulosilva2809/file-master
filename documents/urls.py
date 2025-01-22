from . import views

from django.urls import path


urlpatterns = [
    path(
        'document/room/<int:room_pk>/',
        views.documents_room_detail,
        name='documents_room_detail'
    ),
    path(
        'document/add/room/<int:room_pk>/',
        views.document_add,
        name='document_add'
    ),
    path(
        'document/<int:document_pk>/room/<int:room_pk>/',
        views.document_detail,
        name='document_detail'
    ),
    path(
        'document/<int:document_pk>/edit/room/<int:room_pk>/',
        views.document_edit,
        name='document_edit'
    ),
    path(
        'document/<int:document_pk>/delete/room/<int:room_pk>/',
        views.document_delete,
        name='document_delete'
    ),
    path(
        'document/<int:document_pk>/download/room/<int:room_pk>/',
        views.document_download,
        name='document_download'
    ),
]
