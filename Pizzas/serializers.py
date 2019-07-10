from rest_framework import routers, serializers, viewsets
from Pizzas.models import Pizzas

class PizzasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pizzas
        fields = ('__all__')