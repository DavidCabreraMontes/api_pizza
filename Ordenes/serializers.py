from rest_framework import routers, serializers, viewsets
from Ordenes.models import Ordenes

class OrdenesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ordenes
        fields = ('__all__')