# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import zombies.models


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0021_auto_20160316_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default=None, upload_to=zombies.models.path_and_rename, blank=True),
        ),
    ]