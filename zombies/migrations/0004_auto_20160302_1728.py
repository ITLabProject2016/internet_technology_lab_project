# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0003_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='storypoint',
            name='main_story_id',
            field=models.ForeignKey(default=1, to='zombies.Story'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='story_id',
            field=models.IntegerField(default=1, unique=True, max_length=6),
        ),
    ]
