from rooms.models import Room
from .forms import SectorForm
from .models import Sector

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect


@login_required()
@permission_required('sectors.add_sector', raise_exception=True)
def set_sector(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    sectors = Sector.objects.all().order_by('name')

    if request.method == 'POST':
        form = SectorForm(request.POST)
        if form.is_valid():
            form.save()
            room.sector = form.instance
            room.save()
            messages.success(request, 'Setor criado com sucesso')
            return redirect('room_detail', room.pk)
        else:
            print(form.errors)
            messages.error(request, 'Erro ao adicionar setor')
            return redirect('room_detail', room.pk)
    else:
        form = SectorForm()
    return render(request, 'set_sector.html', {'room': room, 'form': form, 'sectors': sectors})


login_required()
@permission_required('sectors.add_sector', raise_exception=True)
def set_sector_existing(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    sector = get_object_or_404(Sector, pk=request.POST['sector_id'])
    room.sector = sector
    room.save()
    messages.success(request, 'Setor adicionado com sucesso')
    return redirect('room_detail', room.pk)

