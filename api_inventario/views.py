from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import InventarioSerializer
from .models import Inventario
from rest_framework import status
from django.http import Http404

# Aquí está la función index, definida solo una vez
def index(request):
    return render(request, 'index.html')

class Inventario_APIView(APIView):
    
    def post(self, request, format=None):
        serializer = InventarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk, format=None):
        Inventario = self.get_object(pk)
        serializer = InventarioSerializer(Inventario)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        Inventario = self.get_object(pk)
        serializer = InventarioSerializer(Inventario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_410_GONE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk, format=None):
        Inventario = self.get_object(pk)
        Inventario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)