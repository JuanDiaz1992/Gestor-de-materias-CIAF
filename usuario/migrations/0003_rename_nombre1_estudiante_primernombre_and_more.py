# Generated by Django 4.1.2 on 2022-11-22 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_remove_estudiante_primernombre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='nombre1',
            new_name='primerNombre',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='nombre2',
            new_name='segundoNombre',
        ),
    ]