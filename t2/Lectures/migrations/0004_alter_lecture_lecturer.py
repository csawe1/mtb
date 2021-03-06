# Generated by Django 3.2.12 on 2022-03-03 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Lectures', '0003_alter_lecture_lecturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecturer',
            field=models.ForeignKey(default=None, limit_choices_to={'group': 'lecturer'}, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
