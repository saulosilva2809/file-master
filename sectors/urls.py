from . import views
from django.urls import path

urlpatterns = [
    path('set_sector/<int:room_pk>/', views.set_sector, name='set_sector'),
    path('set_sector_existing/<int:room_pk>/', views.set_sector_existing, name='set_sector_existing'),
]
