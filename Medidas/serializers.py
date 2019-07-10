from rest_framework import routers, serializers, viewsets
from Medidas.models import Medidas

class MedidasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medidas
        fields = ('__all__')