from django.db import models
from Usuarios.models import Usuarios
from Carrito.models import Carrito

# Create your models here.

class Ordenes(models.Model):  
    id_Usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    direccion = models.TextField(null=False)
    referencia = models.TextField(null=False)
    total = models.FloatField(null=False)
    pedido = models.ManyToManyField(Carrito, related_name='Carrito')
    tarjeta = models.IntegerField(null=False) #0 = No y 1 = Si
    estado = models.CharField(max_length=50,null=False)
     
    class Meta:
        db_table= "ORDENES"