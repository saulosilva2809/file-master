# Generated by Django 5.1.4 on 2025-01-09 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0001_initial'),
        ('rooms', '0002_room_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='positions.position'),
        ),
    ]
