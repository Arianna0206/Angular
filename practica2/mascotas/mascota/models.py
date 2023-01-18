from django.db import models

# Create your models here.
class mascotas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=255, verbose_name='nombre')
    raza = models.CharField(max_length=200, verbose_name='raza')
    edad = models.IntegerField(verbose_name='edad')
    altura = models.FloatField(verbose_name='altura')
    estaVacunado = models.BooleanField(default=False, verbose_name='estaVacunado')
    
    def _str_(self):
        fila = "nombre: " + self.raza + " - " + self.estaVacunado 
        return fila

        
