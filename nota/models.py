from django.db import models
from datetime import datetime

from nota.choices import gender_choices
# Create your models here.

class Client(models.Model):
    names = models.CharField(max_length = 50, verbose_name = 'Nombres')
    surnames = models.CharField(max_length = 50, verbose_name = 'Apellidos')  
    dui = models.CharField(max_length = 9,unique = True, verbose_name = 'DUI')  
    birthday = models.DateField(default = datetime.now(), verbose_name = 'Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    sexo = models.CharField(max_length=10, choices = gender_choices, default='male', verbose_name='Sexo')

    def _str_ (self):
        return self.names
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'


