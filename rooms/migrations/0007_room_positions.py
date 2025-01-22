# Generated by Django 5.1.4 on 2025-01-13 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0002_remove_position_sector'),
        ('rooms', '0006_alter_room_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='positions',
            field=models.ManyToManyField(related_name='positions', to='positions.position'),
        ),
    ]
