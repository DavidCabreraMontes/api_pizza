from django.shortcuts import render
#======================= MODELOS ===============================
from Medidas.models import Medidas
#======================= Serializers =================================
from Medidas.serializers import MedidasSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class MedidasList(APIView):
    def get(self, request, format=None):
        queryset= Medidas.objects.all()
        serializer = MedidasSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = MedidasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

class MedidasListDetails(APIView):
    def get(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= Medidas.objects.get(pk=pk)
        serializer = MedidasSerializers(queryset)
        return Response(serializer.data)