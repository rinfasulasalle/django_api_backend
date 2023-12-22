from django.db import models
from .usuario import Usuario
from datetime import date

class Trabajador(models.Model):
    usuario_relacionado = models.OneToOneField(Usuario, primary_key=True, on_delete=models.CASCADE)
    trabajador_tipo_documento = models.CharField(max_length=100)
    #trabajador_path_documento = models.FileField(upload_to='docs/identidades/', blank=True, null=True)
    trabajador_nacionalidad = models.CharField(max_length=100, default='No Especificado')
    trabajador_fecha_nacimiento = models.DateField()
    trabajador_ubigeo = models.CharField(max_length=255, default='No Especificado')
    trabajador_sexo = models.CharField(
        max_length=15,
        choices=[
            ('Masculino', 'Masculino'),
            ('Femenino', 'Femenino'),
            ('No Especificado', 'No Especificado'),
        ],
        default='No Especificado'
    )
    trabajador_estado_civil = models.CharField(
        max_length=15,
        choices=[
            ('Soltero', 'Soltero'),
            ('Casado', 'Casado'),
            ('Viudo', 'Viudo'),
            ('Divorciado', 'Divorciado'),
            ('Conviviente', 'Conviviente'),
            ('No Especificado', 'No Especificado'),
        ],
        default='No Especificado'
    )
    #trabajador_path_doc_estado_civil = models.FileField(upload_to='docs/estados_civiles/', blank=True, null=True)
    trabajador_fecha_ingreso_sistema = models.DateField()
    trabajador_fecha_ingreso = models.DateField()
    trabajador_edad = models.IntegerField(default=0)  # por defecto 0, se calculará con save()
    trabajador_record = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # por defecto 0, se calculará con save()
    trabajador_exp_previa = models.DecimalField(max_digits=5, decimal_places=2)  # se ingresa manualmente, es un decimal
    trabajador_total_anios_exp = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # por defecto 0, se calculará con save()

    def save(self, *args, **kwargs):
        # 1. La fecha de ingreso al sistema es la fecha actual
        self.trabajador_fecha_ingreso_sistema = date.today()

        # 2. Calcular la edad en base a la fecha de nacimiento y la fecha actual
        hoy = date.today()
        edad = hoy.year - self.trabajador_fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.trabajador_fecha_nacimiento.month, self.trabajador_fecha_nacimiento.day))
        self.trabajador_edad = edad

        # 3. Calcular trabajador_record
        tiempo_trabajado = hoy - self.trabajador_fecha_ingreso
        record = tiempo_trabajado.days / 365.25
        self.trabajador_record = round(record, 2)

        # 4. Calcular trabajador_total_anios_exp
        self.trabajador_total_anios_exp = self.trabajador_record + float(self.trabajador_exp_previa)

        super(Trabajador, self).save(*args, **kwargs)

    def __str__(self):
        return f"Trabajador: {self.usuario_relacionado}, {self.usuario_relacionado.usuario_nombres} {self.usuario_relacionado.usuario_apellido_paterno} {self.usuario_relacionado.usuario_apellido_materno}"
