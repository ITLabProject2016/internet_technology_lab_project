# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0018_userprofile_finished_stories'),
    ]

    operations = [
        migrations.AddField(
            model_name='storypoint',
            name='ending_type',
            field=models.CharField(max_length=5, null=True, choices=[(b'good', b'good'), (b'bad', b'bad'), (b'none', b'none')]),
            preserve_default=True,
        ),
    ]
