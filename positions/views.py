from rooms.models import Room
from .forms import PositionForm
from .models import Position
from accounts.models import User

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect


def list_positions_room(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    positions = room.positions.all()
    return render(request, 'list_positions_room.html', {'positions': positions, 'room': room})


@login_required()
@permission_required('positions.add_position', raise_exception=True)
def add_position_room(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)

    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            position = form.save(commit=False)
            position.save()
            room.positions.add(position)
            room.save()

            messages.success(request, 'Cargo adicionado com sucesso!')
            return redirect('list_positions_room', room.pk)
        else:
            messages.success(request, 'Erro ao adicionar cargo, tente novamente mais tarde!')
            return redirect('list_positions_room', room.pk)
    else:
        form = PositionForm()
    return render(request, 'add_position_room.html', {'form': form, 'room': room})

    
@login_required()
@permission_required('positions.change_position', raise_exception=True)
def edit_position_room(request, room_pk, position_pk):
    room = get_object_or_404(Room, pk=room_pk)
    position = get_object_or_404(Position, pk=position_pk)

    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            position = form.save(commit=False)
            position.save()
            room.positions.add(position)
            room.save()
            messages.success(request, 'Cargo editado com sucesso!')
            return redirect('list_positions_room', room.pk)
        else:
            messages.success(request, 'Erro ao editar cargo, tente novamente mais tarde!')
            return redirect('list_positions_room', room.pk)
    else:
        form = PositionForm(instance=position)
    return render(request, 'edit_position_room.html', {'form': form, 'room': room})


    
@login_required()
@permission_required('positions.delete_position', raise_exception=True)
def delete_position_room(request, room_pk, position_pk):
    room = get_object_or_404(Room, pk=room_pk)
    position_pk = get_object_or_404(Position, pk=position_pk)

    if request.method == 'POST':
        if room.users.filter(position=position_pk).exists():
            messages.error(request, 'Não é possível remover um cargo que está sendo utilizado por um usuário.')
            return redirect('room_detail', room.pk)

        room.positions.remove(position_pk)
        position_pk.delete()
        room.save()

        messages.success(request, 'Cargo removido com sucesso!')
        return redirect('room_detail', room.pk)
    return render(request, 'delete_position_room.html', {'room': room, 'position': position_pk})


@login_required()
@permission_required('positions.add_position', raise_exception=True)
def set_position_from_user(request, user_pk, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    positions = room.positions.all()
    user = get_object_or_404(User, pk=user_pk)

    if request.method == 'POST':
        position_id = request.POST.get('position_id')
        if position_id:
            position = room.positions.get(pk=position_id)
    
            user.position = position
            user.save()
            
            if user.position:
                messages.success(request, f'Cargo alterado para {position.name} com sucesso!')
            else:
                messages.success(request, f'Cargo {position.name} adicionado com sucesso!')
        else:
            messages.error(request, 'Por favor, selecione um cargo.')
        return redirect('room_detail', room.pk)
    
    return render(request, 'set_position_from_user.html', {
        'selected_user': user,
        'positions': positions,
        'room': room
    })


@login_required()
@permission_required('positions.add_position', raise_exception=True)
def remove_positions_from_user(request, room_pk, user_pk):
    room = get_object_or_404(Room, pk=room_pk)
    user = get_object_or_404(User, pk=user_pk)

    if request.method == 'POST':
        messages.success(request, f'Você removeu o cargo {user.position.name} de {user.username}')
        user.position = None
        user.save()
        return redirect('room_detail', room.pk)
        
    return render(request, 'remove_positions_from_user.html', {'user': user, 'room': room})
