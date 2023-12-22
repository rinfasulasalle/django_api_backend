# Generated by Django 4.2.7 on 2023-12-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_sueldo_sueldo_asigfam_porcentaje_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='trabajador_edad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='trabajador_exp_previa',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='trabajador_record',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='trabajador_total_anios_exp',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
