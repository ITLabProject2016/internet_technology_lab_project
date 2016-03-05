# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0006_auto_20160302_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='story_id',
        ),
        migrations.RemoveField(
            model_name='storypoint',
            name='story_point_id',
        ),
    ]
