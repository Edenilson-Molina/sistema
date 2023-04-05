from django.db import models
from datetime import datetime
# Create your models here.

class Employee(models.Model):
    names = models.CharField(max_length = 30, verbose_name = 'Nombres')  
    dui = models.CharField(max_length = 9,unique = True, verbose_name = 'Nombres')  
    date_joined = models.DateField(default = datetime.now(), verbose_name = 'Fecha de registro')
    age = models.IntegerField(default = 0, verbose_name = 'Edad')
    salary = models.FloatField(default = 0.0, verbose_name = 'Salario')
    state = models.BooleanField(default = True,verbose_name = 'Estado')
    image = models.ImageField(upload_to = 'avatar/%Y/%m/%d', null = True, blank = True, verbose_name = 'Imagen_Perfil')
    cvitae = models.FileField(upload_to = 'cvitae/%Y/%m/%d', null = True, blank = True, verbose_name = 'Hoja de vida')

    def _str_ (self):
        return self.names
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'

