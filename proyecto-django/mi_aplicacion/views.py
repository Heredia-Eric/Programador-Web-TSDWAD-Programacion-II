from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    
    @action(detail=False, methods=['post'])
    def aumentar_precios(self, request):
        porcentaje = request.data.get('porcentaje', 10)
        productos = Producto.objects.all()
        
        for p in productos:
            p.precio = p.precio * (1 + (porcentaje / 100))
            p.save()
            
        return Response({'status': f'Precios aumentados un {porcentaje}%'}, status=status.HTTP_200_OK)