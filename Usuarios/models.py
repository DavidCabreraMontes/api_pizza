from django.db import models
# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=150,null=False)
    correo = models.CharField(max_length=80,null=False,unique=True)
    telefono = models.CharField(max_length=11,null=False)
    class Meta:
        db_table= "USUARIOS"