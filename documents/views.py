import mimetypes
import os

from rooms.models import Room
from documents.models import Document
from .forms import DocumentForm

from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q


@login_required
def documents_room_detail(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    if not request.user in room.users.all():
        messages.error(
            request,
            'Você não tem permissão para acessar esta sala.'
        )
        return redirect('my_rooms')

    documents = room.documents.all().order_by('-date_upload')

    search_query = request.GET.get('search')
    if search_query:
        documents = documents.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        ).distinct()

    context = {
        'room': room,
        'documents': documents,
        'can_add': request.user.has_perm('documents.add_document'),
        'can_change': request.user.has_perm('documents.change_document'),
        'can_delete': request.user.has_perm('documents.delete_document'),
        'can_view': request.user.has_perm('documents.view_document'),
    }

    return render(request, 'documents_room_detail.html', context)


@login_required()
@permission_required('documents.add_document', raise_exception=True)
def document_add(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, room_pk=room_pk)
        if form.is_valid():
            document = form.save(commit=False)
            document.uploader = request.user
            document._room = room
            document.save()
            form.save_m2m()
            messages.success(request, 'Documento adicionado com sucesso!')
            return redirect('room_detail', room.pk)
        else:
            messages.error(
                request,
                'Erro no formulário, tente novamente mais tarde!'
            )
            return redirect('document_add', room.pk)
    else:
        form = DocumentForm(room_pk=room_pk)

        context = {
            'form': form,
            'room': room
        }
        return render(request, 'document_add.html', context)


@login_required()
@permission_required('documents.view_document', raise_exception=True)
def document_detail(request, document_pk, room_pk):
    document = Document.objects.filter(pk=document_pk)
    room = get_object_or_404(Room, pk=room_pk)

    context = {
        'documents': document,
        'room': room
    }

    return render(request, 'documents_room_detail.html', context)


@login_required()
@permission_required('documents.change_document', raise_exception=True)
def document_edit(request, document_pk, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    document = get_object_or_404(Document, pk=document_pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            document = form.save(commit=False)
            form.save_m2m()
            document.save()
            messages.success(
                request,
                f'Documento "{document.name}" atualizado com sucesso!'
            )
            return redirect('room_detail', room.pk)
        else:
            messages.error(
                request,
                'Erro no formulário, tente novamente mais tarde!'
            )
            return redirect('document_detail', document.pk, room.pk)
    else:
        form = DocumentForm(instance=document)
        context = {
            'document': document,
            'form': form,
            'room': room
        }

        return render(request, 'document_edit.html', context)


@login_required()
@permission_required('documents.delete_document', raise_exception=True)
def document_delete(request, document_pk, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    document = get_object_or_404(Document, pk=document_pk)
    if request.method == 'POST':
        document.delete()
        messages.success(request, 'O documento foi excluído com sucesso!')
        return redirect('room_detail', room.pk)

    context = {
        'document': document,
        'room': room
    }

    return render(request, 'document_delete.html', context)


@login_required()
@permission_required('documents.view_document', raise_exception=True)
def document_download(request, room_pk, document_pk):
    room = get_object_or_404(Room, pk=room_pk)
    document = get_object_or_404(Document, pk=document_pk)
    if request.method == 'POST':
        new_filename = request.POST.get('new_filename')
        if new_filename:
            file_path = document.photo.path
            if os.path.exists(file_path):
                mime_type, _ = mimetypes.guess_type(file_path)
                with open(file_path, 'rb') as file:
                    response = HttpResponse(
                        file.read(),
                        content_type=mime_type
                    )

                    response['Content-Disposition'] = f'''
                        attachment; filename="{new_filename}
                        {os.path.splitext(file_path)[1]}
                        "'''
                    return response
            else:
                raise Http404("Arquivo não encontrado.")
        else:
            messages.error(
                request,
                'Por favor, informe um novo nome para o arquivo.'
            )
    context = {
        'document': document,
        'room': room
    }

    return render(request, 'document_download.html', context)
