# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('zombies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storypoint',
            old_name='story_id',
            new_name='story_point_id',
        ),
    ]
