from categories.models import Category
from accounts.models import User

from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    uploader = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    photo = models.FileField(upload_to='documents/')
    description = models.TextField(null=True, blank=True)
    date_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
