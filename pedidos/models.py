from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=32)
    descripcion = models.CharField(max_length=255, null=True)
    from_hour_pedido = models.TimeField(null=True)
    to_hour_pedido = models.TimeField(null=True)
    from_hour_envio = models.TimeField(null=True)
    to_hour_envio = models.TimeField(null=True)
    costo_envio = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    logo = models.ImageField(upload_to='logos', null=True)

class CategoriaMenu(models.Model):
    nombre = models.CharField(max_length=32)

class Menu(models.Model):
    proveedor = models.ForeignKey(Proveedor)
    categoria = models.ForeignKey(CategoriaMenu)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=6, decimal_places=2, null=True)

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True)
    telefono = models.CharField(max_length=20, null=True)
    direccion = models.CharField(max_length=50)


class PedidoMenues(models.Model):
    SOLICITADO = 'FR'
    ACEPTADO = 'AC'
    ENCAMINO = 'DL'
    ENTREGADO = 'EN'
    CANCELADO = 'CA'
    ESTADO_PEDIDO = (
        ('SO', 'Solicitado'),
        ('AC', 'Aceptado'),
        ('EN', 'En Camino'),
        ('EN', 'Entregado'),
        ('CA', 'Cancelado'),
    )

    proveedor = models.ForeignKey(Proveedor)
    cliente = models.ForeignKey(Cliente)
    menues = models.ManyToManyField(Menu)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_PEDIDO,
        default=SOLICITADO,
    )
    comentario = models.CharField(max_length=255, null=True)
    hora_entrega = models.TimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





