# Generated by Django 5.1.4 on 2025-01-16 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('remove_user_room', 'Remove usuário da sala')]},
        ),
    ]
