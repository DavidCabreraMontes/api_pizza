from rest_framework import routers, serializers, viewsets
from Usuarios.models import Usuarios

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('__all__')