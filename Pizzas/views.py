from django.shortcuts import render
#======================= MODELOS ===============================
from Pizzas.models import Pizzas
#======================= Serializers =================================
from Pizzas.serializers import PizzasSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class PizzasList(APIView):
    def get(self, request, format=None):
        queryset= Pizzas.objects.all()
        serializer = PizzasSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post (self, request, format=None):
        serializer = PizzasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response (response, status=status.HTTP_400_BAD_REQUEST)

class PizzasDetails(APIView):
    def get(self, request,*args, **kwargs):
        pk = kwargs.get('pk')
        print(pk) 
        queryset= Pizzas.objects.get(pk=pk)
        serializer = PizzasSerializers(queryset)
        return Response(serializer.data)