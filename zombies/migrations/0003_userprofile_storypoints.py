# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombies', '0002_storypoints'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile_StoryPoints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('storypoint', models.ForeignKey(to='zombies.StoryPoints')),
                ('user', models.ForeignKey(to='zombies.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
