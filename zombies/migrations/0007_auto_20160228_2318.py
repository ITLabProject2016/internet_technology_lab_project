# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0006_auto_20160228_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storypoint',
            name='parent_storypoint_id',
            field=models.ForeignKey(to='zombies.StoryPoint', blank=True),
        ),
    ]
