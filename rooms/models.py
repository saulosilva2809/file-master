from accounts.models import User
from categories.models import Category
from documents.models import Document
from positions.models import Position
from sectors.models import Sector

from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='owner', null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, null=True, blank=True)
    positions = models.ManyToManyField(Position, related_name='positions', null=True, blank=True)
    users = models.ManyToManyField(User, related_name='users')
    documents = models.ManyToManyField(Document)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
