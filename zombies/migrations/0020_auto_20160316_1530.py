# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0019_storypoint_ending_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='picture',
            field=models.ImageField(default=None, width_field=300, upload_to=b'img/story', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='storypoint',
            name='picture',
            field=models.ImageField(default=None, width_field=300, upload_to=b'img/story_point', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default=None, width_field=300, upload_to=b'img/profile', blank=True),
        ),
    ]
