from django.db import models

class DatosGlobales(models.Model):
    id = models.AutoField(primary_key=True)
    anio = models.PositiveSmallIntegerField() 
    remuneracion_minima_vital = models.DecimalField(max_digits=10, decimal_places=2)
    uit = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Dato Global Año: {self.anio} :  {self.remuneracion_minima_vital} - {self.uit}"
