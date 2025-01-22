from app.utils import get_password
from app.utils import user_in_room, is_room_creator
from accounts.models import User
from .forms import RoomForm
from .models import Room

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.shortcuts import render, get_object_or_404, redirect


@login_required()
def create_room_password_access(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == get_password():
            user = request.user
            user.room_creator = True
            user.save()
            return redirect('create_room')
        else:
            messages.error(request, 'Senha inválida!')
            return redirect('create_room')
    return render(request, 'rooms/create_room_password_access.html')


@is_room_creator
@login_required()
def create_room(request):
    permissions = Permission.objects.all()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            request.user.user_permissions.set(permissions)
            request.user.save()

            form.instance.owner = request.user
            form.instance.users.add(request.user)
            form.instance.save()
            return redirect('room_detail', form.instance.pk)
        else:
            messages.error(request, 'Erro ao criar sala!')
            return redirect('create_room')
    else:
        form = RoomForm()
        return render(request, 'rooms/create_room.html', {'form': form})


@login_required()
def connect_room(request):
    room = Room.objects.all()
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        room_password = request.POST.get('room_password')

        room = Room.objects.get(name=room_name)
        if room:
            if room.password == room_password:
                room.users.add(request.user)
                room.save()
                messages.success(request, 'Você entrou na sala com sucesso!')
                return redirect('room_detail', room.pk)
            else:
                messages.error(request, 'Senha incorreta!')
                return redirect('room_detail', room.pk)
        else:
            messages.error(request, 'Senha não encontrada!')
            return redirect('room_detail', room.pk)
    else:
        return render(request, 'rooms/connect_room.html', {'room': room})


@user_in_room
@login_required()
def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    categories = room.categories.all()

    context = {
        'room': room, 
        'categories': categories,
        'can_add': request.user.has_perm('categories.add_category'),
        'can_change': request.user.has_perm('categories.change_category'),
        'can_delete': request.user.has_perm('categories.delete_category'),
        'can_view': request.user.has_perm('categories.view_category'),
    }

    return render(request, 'rooms/room_detail.html', context)


@login_required()
def my_rooms(request):
    user = request.user
    rooms = Room.objects.filter(users=user)
    return render(request, 'rooms/my_rooms.html', {'rooms': rooms})


@login_required()
@permission_required('accounts.remove_user_room', raise_exception=True)
def remove_user_from_room(request, room_pk, user_pk):
    room = get_object_or_404(Room, pk=room_pk)
    user_to_remove = get_object_or_404(User, pk=user_pk)

    if request.method == 'POST':
        if user_to_remove != room.owner:  # Não permite remover o dono da sala
            room.users.remove(user_to_remove)
            messages.success(request, f'Usuário {user_to_remove.username} removido com sucesso!')
        else:
            messages.error(request, 'Não é possível remover o proprietário da sala!')
        return redirect('room_detail', room.pk)
    
    return render(request, 'rooms/remove_user.html', {'room': room, 'user_to_remove': user_to_remove})
