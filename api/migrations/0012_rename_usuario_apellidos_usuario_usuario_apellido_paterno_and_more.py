# Generated by Django 4.2.7 on 2023-12-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_trabajador_trabajador_path_doc_estado_civil_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario_apellidos',
            new_name='usuario_apellido_paterno',
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuario_apellido_materno',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
