# models/sueldo.py
from django.db import models
from .trabajador import Trabajador
from decimal import Decimal


class Sueldo(models.Model):
    trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE, unique=True)
    id = models.AutoField(primary_key=True)
    sueldo_valor_basico = models.DecimalField(max_digits=20, decimal_places=2)
    sueldo_opc_asigfam = models.BooleanField(default=False)
    sueldo_opc_bono = models.BooleanField(default=False)
    sueldo_porcentaje_bono = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    sueldo_monto_asigfam = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    sueldo_monto_bono = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    sueldo_mensual = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    sueldo_anual = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)

    def save(self, *args, **kwargs):
        # Calcula sueldo_monto_asigfam y sueldo_monto_bono
        if not self.sueldo_opc_asigfam:
            self.sueldo_monto_asigfam = 0.0
        else:
            self.sueldo_monto_asigfam = self.sueldo_valor_basico * Decimal('0.2')

        if not self.sueldo_opc_bono:
            self.sueldo_monto_bono = 0.0
        else:
            self.sueldo_monto_bono = self.sueldo_valor_basico * self.sueldo_porcentaje_bono

        # Calcula sueldo_mensual y sueldo_anual
        self.sueldo_mensual = (
            self.sueldo_valor_basico +
            Decimal(str(self.sueldo_monto_asigfam)) +
            Decimal(str(self.sueldo_monto_bono))
        )
        self.sueldo_anual = self.sueldo_mensual * 14

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Sueldo: {self.id} - {self.trabajador.usuario_relacionado.id}"
