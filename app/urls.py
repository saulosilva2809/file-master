"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        'permission/',
        views.permission_access_app,
        name='permission_access_app'
    ),
    path('', views.home, name='home'),
    path('access_denied/', views.access_denied, name='access_denied'),

    path('accounts/', include('accounts.urls')),
    path('rooms/', include('rooms.urls')),
    path('documents/', include('documents.urls')),
    path('categories/', include('categories.urls')),
    path('sectors/', include('sectors.urls')),
    path('positions/', include('positions.urls')),
    path('permissions/', include('permissions.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
