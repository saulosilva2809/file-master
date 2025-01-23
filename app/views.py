from .utils import get_password_access_app

from django.contrib import messages
from django.shortcuts import render, redirect


def custom_403(request, exception=None):
    return render(request, '403.html', status=403)


def custom_404(request, exception=None):
    return render(request, '404.html', status=404)


def permission_access_app(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == get_password_access_app():
            request.session['is_authorized'] = True
            return redirect('home')
        else:
            messages.error(request, 'Senha inválida!')

    return render(request, 'permission_access_app.html')


def home(request):
    return render(request, 'home.html')


def access_denied(request):
    return render(request, 'access_denied.html')
