from .models import RoomUserPermission


def has_room_permission(user, room, permission):
    """
    Verifica se um usuário tem uma permissão específica em uma sala.
    
    Args:
        user: O usuário a ser verificado
        room: A sala onde verificar a permissão
        permission: A permissão a ser verificada (ex: 'add_document')
        
    Returns:
        bool: True se o usuário tem a permissão, False caso contrário
    """
    try:
        room_permission = RoomUserPermission.objects.get(user=user, room=room)
        return room_permission.has_perm(permission)
    except RoomUserPermission.DoesNotExist:
        return False


def get_room_permissions(user, room):
    """
    Retorna todas as permissões que um usuário tem em uma sala específica.
    
    Args:
        user: O usuário
        room: A sala
        
    Returns:
        QuerySet: QuerySet com todas as permissões do usuário na sala
    """
    try:
        room_permission = RoomUserPermission.objects.get(user=user, room=room)
        return room_permission.permissions.all()
    except RoomUserPermission.DoesNotExist:
        return []


def set_room_permission(user, room, permission, grant=True):
    """
    Adiciona ou remove uma permissão de um usuário em uma sala.
    
    Args:
        user: O usuário
        room: A sala
        permission: A permissão a ser adicionada/removida
        grant: True para adicionar, False para remover
    """
    room_permission, created = RoomUserPermission.objects.get_or_create(
        user=user,
        room=room
    )
    
    if grant:
        room_permission.add_perm(permission)
    else:
        room_permission.remove_perm(permission) 