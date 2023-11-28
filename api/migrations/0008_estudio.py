# Generated by Django 4.2.7 on 2023-11-28 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_direccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estudio_fecha_colegiatura', models.DateField(blank=True, null=True)),
                ('estudio_condicion', models.CharField(choices=[('Habilitado', 'Habilitado'), ('No habilitado', 'No habilitado'), ('XXXXX', 'XXXXX')], default='XXXXX', max_length=15)),
                ('id_carrera_educativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdowncarreras')),
                ('id_estudio_capacitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdowncapacitaciones')),
                ('id_estudio_especializacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdownespecializaciones')),
                ('id_estudio_nivel_educativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdownniveleducativo')),
                ('id_estudio_situacion_especial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdownsituacionesespeciales')),
                ('id_institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdowninstituciones')),
                ('id_regimen_aseguramiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdownregimenaseguramiento')),
                ('id_regimen_laboral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdownregimenlaboral')),
                ('id_sede_colegiatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dropdownsedes')),
                ('trabajador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.trabajador')),
            ],
        ),
    ]