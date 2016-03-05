# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0008_auto_20160305_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='visits',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='storypoint',
            name='visits',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
