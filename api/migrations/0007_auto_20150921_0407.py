# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20150921_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='tipo',
            field=models.OneToOneField(null=True, db_column=b'fk_tipo', blank=True, to='api.TipoMascota'),
        ),
    ]
