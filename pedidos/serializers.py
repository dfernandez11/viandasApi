# Serializers define the API representation.
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from pedidos.models import Proveedor, Cliente, CategoriaMenu, Menu, PedidoMenues

class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('nombre', 'descripcion', 'from_hour_pedido', 'to_hour_pedido', 'from_hour_envio', 'to_hour_envio',
                  'costo_envio', 'logo' )


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido', 'email', 'telefono', 'direccion')

class CategoriaMenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoriaMenu
        fields = ('nombre',)


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class PedidosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PedidoMenues
        fields = '__all__'



