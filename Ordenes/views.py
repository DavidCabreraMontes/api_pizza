from django.shortcuts import render
#======================= MODELOS ===============================
from Ordenes.models import Ordenes
#======================= Serializers =================================
from Ordenes.serializers import OrdenesSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class OrdenesList(APIView):
    def get(self, request, format=None):
        queryset= Ordenes.objects.all()
        serializer = OrdenesSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = OrdenesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

class OrdenesListAuthor(APIView):
    def get(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= Ordenes.objects.get(pk=pk)
        serializer = OrdenesSerializers(queryset)
        return Response(serializer.data)
    
    def put (self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        profile = Ordenes.objects.get(pk=pk)
        serializer = OrdenesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)