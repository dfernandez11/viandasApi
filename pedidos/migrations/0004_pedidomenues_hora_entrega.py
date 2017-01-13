# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_pedidomenues'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidomenues',
            name='hora_entrega',
            field=models.TimeField(null=True),
        ),
    ]
