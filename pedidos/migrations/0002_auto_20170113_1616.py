# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaMenu',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('telefono', models.CharField(max_length=20, null=True)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('categoria', models.ForeignKey(to='pedidos.CategoriaMenu')),
            ],
        ),
        migrations.RemoveField(
            model_name='carta',
            name='proveedeor',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='costo_envio',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='descripcion',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='from_hour_envio',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='from_hour_pedido',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='logo',
            field=models.ImageField(null=True, upload_to='logos'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='to_hour_envio',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='to_hour_pedido',
            field=models.TimeField(null=True),
        ),
        migrations.DeleteModel(
            name='Carta',
        ),
        migrations.AddField(
            model_name='menu',
            name='proveedor',
            field=models.ForeignKey(to='pedidos.Proveedor'),
        ),
    ]
