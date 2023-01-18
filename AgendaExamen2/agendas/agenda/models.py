from django.db import models

# Create your models here.
class agendas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name='nombre')
    fecha = models.CharField(max_length=200, verbose_name='fecha')
    tipo = models.CharField(max_length=200, verbose_name='tipo')
    descripcion = models.CharField(max_length=200, verbose_name='descripcion', null=True)
    
    def _str_(self):
        return self.nombre

    

    