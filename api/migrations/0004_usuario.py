# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'usuario_id')),
                ('email', models.CharField(max_length=50, db_column=b'email', blank=True)),
                ('facebook_id', models.CharField(max_length=20, db_column=b'facebook_id', blank=True)),
                ('estado', models.SmallIntegerField(null=True, db_column=b'estado', blank=True)),
                ('telefono', models.CharField(max_length=20, db_column=b'telefono', blank=True)),
                ('fecha_registro', models.DateField(null=True, db_column=b'fecha_registro', blank=True)),
                ('direccion', models.CharField(max_length=120, null=True, db_column=b'direccion', blank=True)),
                ('foto_perfil_url', models.CharField(max_length=150, null=True, db_column=b'foto_perfil_url', blank=True)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'usuario',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
