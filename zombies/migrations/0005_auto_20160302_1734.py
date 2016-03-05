# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('zombies', '0004_auto_20160302_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='story_id',
            field=models.IntegerField(unique=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='storypoint',
            name='main_story_id',
            field=models.ForeignKey(to='zombies.Story'),
        ),
    ]
