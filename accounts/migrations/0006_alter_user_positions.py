# Generated by Django 5.1.4 on 2025-01-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_positions'),
        ('positions', '0002_remove_position_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='positions',
            field=models.ManyToManyField(blank=True, to='positions.position'),
        ),
    ]
