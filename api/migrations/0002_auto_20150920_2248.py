# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto_perfil_url',
            field=models.CharField(max_length=150, null=True, db_column=b'foto_perfil_url', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(max_length=120, null=True, db_column=b'direccion', blank=True),
        ),
    ]
