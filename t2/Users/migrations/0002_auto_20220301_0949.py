# Generated by Django 3.2.12 on 2022-03-01 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
