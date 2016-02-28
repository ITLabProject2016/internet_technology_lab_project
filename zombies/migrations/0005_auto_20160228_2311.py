# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0004_auto_20160228_2308'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StoryPoints',
            new_name='StoryPoint',
        ),
        migrations.RenameModel(
            old_name='UserProfile_StoryPoints',
            new_name='UserProfile_StoryPoint',
        ),
    ]
