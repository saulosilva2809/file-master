from rooms.models import Room
from accounts.models import User

from django.contrib import messages
from django.contrib.auth.models import Permission
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required


@login_required
def list_perms_room(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    return render(request, 'list_perms_room.html', {'room': room})


@login_required
@permission_required('auth.add_permission', raise_exception=True)
def add_perms_from_user(request, room_pk, user_pk):
    room = get_object_or_404(Room, pk=room_pk)
    user = get_object_or_404(User, pk=user_pk)
    permissions = Permission.objects.all().order_by('content_type__app_label', 'content_type__model')
    user_permissions = user.user_permissions.all()
    
    if request.method == 'POST':
        selected_permissions = request.POST.getlist('permissions')
        # Remove todas as permissões existentes
        user.user_permissions.clear()
        
        if selected_permissions:
            # Adiciona as novas permissões selecionadas
            for perm_id in selected_permissions:
                permission = Permission.objects.get(id=perm_id)
                user.user_permissions.add(permission)
            messages.success(request, 'Permissões atualizadas com sucesso!')
            return redirect('list_perms_room', room.pk)
        else:
            messages.error(request, 'Selecione pelo menos uma permissão.')
    
    return render(request, 'add_perms_from_user.html', {
        'permissions': permissions,
        'room': room,
        'selected_user': user,
        'user_permissions': user_permissions
    })


@login_required
@permission_required('auth.delete_permission', raise_exception=True)
def remove_perms_from_user(request, room_pk, user_pk):
    room = get_object_or_404(Room, pk=room_pk)
    user = get_object_or_404(User, pk=user_pk)
    user_permissions = user.user_permissions.all()
    
    if request.method == 'POST':
        selected_permissions = request.POST.getlist('permissions')
        if selected_permissions:
            # Remove apenas as permissões selecionadas
            for perm_id in selected_permissions:
                permission = Permission.objects.get(id=perm_id)
                user.user_permissions.remove(permission)
            messages.success(request, 'Permissões removidas com sucesso!')
            return redirect('list_perms_room', room.pk)
        else:
            messages.error(request, 'Selecione pelo menos uma permissão para remover.')
    
    return render(request, 'remove_perms_from_user.html', {
        'room': room,
        'selected_user': user,
        'user_permissions': user_permissions
    })
