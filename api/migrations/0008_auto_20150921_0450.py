# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150921_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='tipo',
            field=models.ForeignKey(db_column=b'fk_tipo', blank=True, to='api.TipoMascota', null=True),
        ),
    ]
