from rest_framework import routers, serializers, viewsets

# ViewSets define the view behavior.
from pedidos.models import Proveedor
from pedidos.serializers import ProveedorSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
