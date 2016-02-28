# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0003_userprofile_storypoints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storypoints',
            name='parent_storypoint_id',
            field=models.ForeignKey(to='zombies.StoryPoints', null=True),
        ),
        migrations.AlterField(
            model_name='storypoints',
            name='photo',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='storypoints',
            name='story_choices',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
