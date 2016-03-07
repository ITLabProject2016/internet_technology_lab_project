# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0012_remove_storypoint_endings'),
    ]

    operations = [
        migrations.AddField(
            model_name='storypoint',
            name='endings',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
