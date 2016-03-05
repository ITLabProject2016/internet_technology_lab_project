# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0007_auto_20160305_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storypoint',
            name='story_type',
            field=models.CharField(max_length=5, choices=[(b'start', b'start'), (b'mid', b'mid'), (b'end', b'end')]),
        ),
    ]
