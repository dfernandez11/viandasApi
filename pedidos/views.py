from rest_framework import routers, serializers, viewsets, generics

# ViewSets define the view behavior.
from pedidos.models import Proveedor, Cliente, CategoriaMenu, Menu, PedidoMenues
from pedidos.serializers import ProveedorSerializer, ClienteSerializer, CategoriaMenuSerializer, MenuSerializer, PedidosSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CategoriaMenuViewSet(viewsets.ModelViewSet):
    queryset = CategoriaMenu.objects.all()
    serializer_class = CategoriaMenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuList(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        prove = self.kwargs['prove']
        return Menu.objects.filter(proveedor=prove)

class PedidoMenuesViewSet(viewsets.ModelViewSet):
    queryset = PedidoMenues.objects.all()
    serializer_class = PedidosSerializer
