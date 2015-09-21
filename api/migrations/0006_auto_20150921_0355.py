# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150921_0048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='fk_tipo',
            new_name='tipo',
        ),
    ]
