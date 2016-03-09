# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0017_auto_20160308_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='finished_stories',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
