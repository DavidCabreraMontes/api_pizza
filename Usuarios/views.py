from django.shortcuts import render
#======================= MODELOS ===============================
from Usuarios.models import Usuarios
#======================= Serializers =================================
from Usuarios.serializers import UsuariosSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class UsuariosList(APIView):
    def get(self, request, format=None):
        queryset= Usuarios.objects.all()
        serializer = UsuariosSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = UsuariosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

class UsuariosDetails(APIView):
    def get(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= Usuarios.objects.get(pk=pk)
        serializer = UsuariosSerializers(queryset)
        return Response(serializer.data)
    
    def put (self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        profile = Usuarios.objects.get(pk=pk)
        serializer = UsuariosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)