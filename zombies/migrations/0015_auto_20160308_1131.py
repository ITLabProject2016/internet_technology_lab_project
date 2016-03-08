# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0014_remove_storypoint_endings'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='test',
            field=models.CharField(default=b'Test', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
