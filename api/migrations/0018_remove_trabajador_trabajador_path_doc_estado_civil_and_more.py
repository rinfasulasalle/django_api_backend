# Generated by Django 4.2.7 on 2023-12-22 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_trabajador_trabajador_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajador',
            name='trabajador_path_doc_estado_civil',
        ),
        migrations.RemoveField(
            model_name='trabajador',
            name='trabajador_path_documento',
        ),
    ]
