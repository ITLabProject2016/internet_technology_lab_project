# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0009_auto_20160305_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='storypoint',
            name='story_point_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
