# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150920_2248'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
