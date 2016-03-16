# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0020_auto_20160316_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='picture',
            field=models.ImageField(default=None, upload_to=b'img/story', blank=True),
        ),
        migrations.AlterField(
            model_name='storypoint',
            name='picture',
            field=models.ImageField(default=None, upload_to=b'img/story_point', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default=None, upload_to=b'img/profile', blank=True),
        ),
    ]
