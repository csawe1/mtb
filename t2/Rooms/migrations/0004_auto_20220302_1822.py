# Generated by Django 3.2.12 on 2022-03-02 15:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0003_room_eth_s'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='state',
        ),
        migrations.AddField(
            model_name='room',
            name='time_occupied',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), blank=True, default='7:0:0', size=None),
            preserve_default=False,
        ),
    ]