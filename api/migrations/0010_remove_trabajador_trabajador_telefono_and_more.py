# Generated by Django 4.2.7 on 2023-11-28 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_datosglobales'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajador',
            name='trabajador_telefono',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='usuario_sexo',
        ),
    ]