# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'mascota_id')),
                ('nombre', models.CharField(max_length=50, db_column=b'nombre', blank=True)),
                ('raza', models.CharField(max_length=50, db_column=b'raza', blank=True)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'mascota',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'publicacion_id')),
                ('en_transito', models.CharField(max_length=1, db_column=b'en_transito', blank=True)),
                ('fecha_publicacion', models.DateField(null=True, db_column=b'fecha_publicacion', blank=True)),
                ('estado', models.SmallIntegerField(null=True, db_column=b'estado', blank=True)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'publicacion',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoAviso',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'tipo_id')),
                ('tipo', models.CharField(max_length=50, db_column=b'tipo', blank=True)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'tipo_aviso',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoMascota',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'tipo_id')),
                ('tipo', models.CharField(max_length=20, db_column=b'tipo', blank=True)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'tipo_mascota',
                'managed': True,
            },
            bases=(models.Model,),
        ),
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
        migrations.AddField(
            model_name='publicacion',
            name='fk_aviso',
            field=models.ForeignKey(db_column=b'fk_aviso', blank=True, to='api.TipoAviso', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicacion',
            name='fk_mascota',
            field=models.ForeignKey(db_column=b'fk_mascota', blank=True, to='api.Mascota', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publicacion',
            name='fk_usuario',
            field=models.ForeignKey(db_column=b'fk_usuario', blank=True, to='api.Usuario', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mascota',
            name='tipo',
            field=models.ForeignKey(db_column=b'fk_tipo', blank=True, to='api.TipoMascota', null=True),
            preserve_default=True,
        ),
    ]
