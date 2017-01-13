from django.contrib import admin
from pedidos.models import Proveedor, CategoriaMenu, Menu, Cliente, PedidoMenues

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(CategoriaMenu)
admin.site.register(Menu)
admin.site.register(Cliente)
admin.site.register(PedidoMenues)