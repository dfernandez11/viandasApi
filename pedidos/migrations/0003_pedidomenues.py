# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20170113_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoMenues',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('estado', models.CharField(default='FR', max_length=2, choices=[('SOLICITADO', 'Solicitado'), ('ACEPTADO', 'Aceptado'), ('ENCAMINO', 'En Camino'), ('ENTREGADO', 'Entregado'), ('CANCELADO', 'Cancelado')])),
                ('comentario', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(to='pedidos.Cliente')),
                ('menues', models.ManyToManyField(to='pedidos.Menu')),
                ('proveedor', models.ForeignKey(to='pedidos.Proveedor')),
            ],
        ),
    ]
