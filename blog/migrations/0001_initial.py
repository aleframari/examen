# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isbn', models.CharField(max_length=60)),
                ('titutlo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('editorial', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_prestamo', models.DateTimeField(auto_now=True, null=True)),
                ('fecha_devolulcion', models.DateTimeField(max_length=50)),
                ('fecha_devolucionreal', models.DateTimeField(max_length=50)),
                ('libro', models.ForeignKey(to='blog.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('dpi', models.TextField()),
                ('libro', models.ManyToManyField(to='blog.Libro', through='blog.Prestamo')),
            ],
        ),
        migrations.AddField(
            model_name='prestamo',
            name='usuario',
            field=models.ForeignKey(to='blog.Usuario'),
        ),
    ]
