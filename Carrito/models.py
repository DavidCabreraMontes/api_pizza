from django.db import models
from Pizzas.models import Pizzas
from Medidas.models import Medidas
from Usuarios.models import Usuarios
# Create your models here.

class Carrito(models.Model):
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    medida = models.ForeignKey(Medidas, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    precio = models.FloatField(null=False)
    
    class Meta:
        db_table= "CARRITO"