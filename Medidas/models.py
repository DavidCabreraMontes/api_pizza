from django.db import models
# Create your models here.

class Medidas(models.Model):
    nombre = models.CharField(max_length=150,null=False, unique=True)
    precio = models.FloatField(null=False)
    
    class Meta:
        db_table= "MEDIDAS"