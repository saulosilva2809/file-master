from .forms import CategoryForm
from .models import Category
from rooms.models import Room

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect


@login_required()
def categories_room_detail(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    name = request.POST.get('document_search')
    categories = None

    if name:
        categories = room.categories.filter(name__icontains=name)

    context = {
        'room': room,
        'categories': categories,
        'query': name
    }

    return render(request, 'categories_room_detail.html', context)


@login_required()
@permission_required('categories.add_category', raise_exception=True)
def category_add(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            form.save()
            room.categories.add(category)
            messages.success(request, 'Categoria criada com sucesso!')
            return redirect('room_detail', room.pk)
        else:
            messages.error(
                request,
                'Erro no form. Tente novamente mais tarde!'
            )
            return redirect('room_detail', room.pk)
    else:
        form = CategoryForm()
        context = {
            'room': room,
            'form': form
        }
        return render(request, 'category_add.html', context)


@login_required()
@permission_required('categories.change_category', raise_exception=True)
def category_edit(request, category_pk, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    category = get_object_or_404(Category, pk=category_pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso!')
            return redirect('room_detail', room.pk)
        else:
            messages.error(
                request,
                'Erro no form. Tente novamente mais tarde!'
            )
            return redirect('room_detail', room.pk)
    else:
        form = CategoryForm(instance=category)
        context = {
            'room': room,
            'form': form,
            'category': category
        }
        return render(request, 'category_edit.html', context)


@login_required()
@permission_required('categories.delete_category', raise_exception=True)
def category_delete(request, category_pk, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    category = get_object_or_404(Category, pk=category_pk)

    if request.method == 'POST':
        category.delete()
        messages.success(request, 'A categoria foi excluída com sucesso!')
        return redirect('room_detail', room.pk)

    context = {
        'category': category,
        'room': room
    }

    return render(request, 'category_delete.html', context)
