# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_pedidomenues_hora_entrega'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidomenues',
            name='estado',
            field=models.CharField(max_length=20, default='FR', choices=[('SO', 'Solicitado'), ('AC', 'Aceptado'), ('EN', 'En Camino'), ('EN', 'Entregado'), ('CA', 'Cancelado')]),
        ),
    ]
