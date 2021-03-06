# Generated by Django 3.2.12 on 2022-03-11 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lectures', '0004_alter_lecture_lecturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 12, 49, 19, 709535)),
        ),
        migrations.AddField(
            model_name='lecture',
            name='reason',
            field=models.CharField(choices=[('lecture', 'Normal lecture'), ('CAT', 'I want to hold a cat in the room'), ('Private class meeting', 'I want to hold a private meeting in the selected room'), ('Group Discussion', 'I want to hold a group study session in the selected room')], default='class', max_length=30),
            preserve_default=False,
        ),
    ]
