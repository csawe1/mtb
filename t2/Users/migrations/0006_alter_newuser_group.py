# Generated by Django 3.2.12 on 2022-03-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_alter_newuser_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='group',
            field=models.CharField(choices=[('student', 'Student'), ('lecturer', 'Lecturer'), ('admin', 'Admin')], max_length=9),
        ),
    ]
