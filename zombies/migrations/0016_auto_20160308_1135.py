# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0015_auto_20160308_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='test',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='exp',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
