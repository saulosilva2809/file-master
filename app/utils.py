import json
import logging
import os
from app.settings import BASE_DIR
from rooms.models import Room

from django.contrib import messages
from django.shortcuts import redirect


logger = logging.getLogger(__name__)


def user_in_room(view_func):
    def _wrapped_view(request, *args, **kwargs):
        room_id = kwargs.get('pk')
        logger.info(
            f"""
            Verificando permissão para o usuário
            {request.user.username} na sala {room_id}
            """
        )
        try:
            room = Room.objects.get(id=room_id)
            logger.info(f"Sala encontrada: {room.name}")
            if request.user in room.users.all():
                logger.info("Usuário está na sala")
                return view_func(request, *args, **kwargs)
            else:
                logger.info("Usuário não está na sala")
                messages.error(
                    request,
                    "Você não tem permissão para ver esta sala."
                )

                return redirect('access_denied')
        except Room.DoesNotExist:
            logger.info(f"Sala com ID {room_id} não encontrada.")
            messages.error(request, f"Sala com ID {room_id} não encontrada.")
            return redirect('access_denied')
    return _wrapped_view


def is_room_creator(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.room_creator:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(
                request,
                "Você não tem permissão para criar uma sala."
            )
            return redirect('access_denied')
    return _wrapped_view


def get_password(filename=os.path.join(BASE_DIR, 'secrets/password.json')):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data.get('password')


def get_password_access_app(filename=os.path.join(
        BASE_DIR, 'secrets/password.json'
        )):

    with open(filename, 'r') as file:
        data = json.load(file)
        return data.get('permission')
