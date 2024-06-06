from rest_framework import viewsets
from .serializer import Tipo_ProductoSerializer, StockSerializer, ProductoSerializer
from .models import Tipo_Producto,Stock,Producto
# Create your views here.
#clases propias de la api
from rest_framework.decorators import api_view,permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
##PARA LA AUTENTICACION

class Tipo_ProductoViewSet(viewsets.ModelViewSet):
    queryset= Tipo_Producto.objects.all()
    serializer_class = Tipo_ProductoSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset= Stock.objects.all()
    serializer_class = StockSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset= Producto.objects.all()
    serializer_class = ProductoSerializer


csrf_exempt
@api_view(['GET','POST'])
def lista_Productos(request):
    ##siempre se pregunta que tipo de metodo es el que trabajara
    if request.method =='GET':
        query=Producto.objects.all()
        serializer = ProductoSerializer(query, many=True)
        return Response(serializer.data)
    elif request.method =='POST': 
         serializer = ProductoSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED) 
         else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)      

@api_view(['GET','PUT','DELETE'])
def detalle_Producto(request, id):
    try:
        producto =Producto.objects.get(nombre=id)
    except producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
    if request.method =='GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    if request.method =='PUT':
        serializer = ProductoSerializer(producto, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    if request.method =='DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
