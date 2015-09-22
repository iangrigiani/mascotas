# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20150921_0450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='fk_tipo',
            new_name='tipo',
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='fk_aviso',
            new_name='aviso',
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='fk_mascota',
            new_name='mascota',
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='fk_usuario',
            new_name='usuario',
        ),
    ]
