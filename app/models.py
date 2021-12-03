from django.db import models

# Create your models here.
class Modelo(models.Model):
    codigo=models.CharField("Código",max_length=10,unique=True)
    descripcion=models.CharField("Descripción",max_length=50)

    def __str__(self):
        return self.codigo
    
    class Meta:
        verbose_name_plural= "Modelos"

        