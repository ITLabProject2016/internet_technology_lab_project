# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0011_storypoint_endings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storypoint',
            name='endings',
        ),
    ]
