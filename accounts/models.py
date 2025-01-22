from positions.models import Position

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    room_creator = models.BooleanField(default=False)
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        permissions = [
            ('remove_user_room', 'Can remove user room')
        ]

    def __str__(self):
        return self.username
