from django.db import models
# Create your models here.

class Pizzas(models.Model):
    nombre = models.CharField(max_length=150,null=False, unique=True)
    ingredientes=models.TextField(null=False)
    descripcion=models.TextField(null=False)
    precio = models.FloatField(null=False)
    class Meta:
        db_table= "PIZZAS"