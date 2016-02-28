# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryPoints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('photo', models.CharField(max_length=128)),
                ('story_description', models.CharField(max_length=2500)),
                ('story_choices', models.CharField(max_length=300)),
                ('parent_storypoint_id', models.ForeignKey(to='zombies.StoryPoints')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
