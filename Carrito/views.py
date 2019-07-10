from django.shortcuts import render
#======================= MODELOS ===============================
from Carrito.models import Carrito
#======================= Serializers =================================
from Carrito.serializers import CarritoSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class CarritoList(APIView):
    def get(self, request, format=None):
        queryset= Carrito.objects.all()
        serializer = CarritoSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = CarritoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

class CarritoListUser(APIView):
    def get(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= Carrito.objects.get(pk=pk)
        serializer = CarritoSerializers(queryset)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        profile = Carrito.objects.get(pk=pk)
        profile.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)