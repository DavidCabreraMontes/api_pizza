from rest_framework import routers, serializers, viewsets
from Carrito.models import Carrito

class CarritoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = ('__all__')