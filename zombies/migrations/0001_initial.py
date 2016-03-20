# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import zombies.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('picture', models.ImageField(default=None, upload_to=b'img/story', blank=True)),
                ('visits', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Stories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoryPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('story_point_id', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=1000)),
                ('picture', models.ImageField(default=None, upload_to=b'img/story_point', blank=True)),
                ('choiceText', models.CharField(max_length=100, null=True, blank=True)),
                ('experience', models.IntegerField(default=0)),
                ('story_type', models.CharField(max_length=5, choices=[(b'start', b'start'), (b'mid', b'mid'), (b'end', b'end')])),
                ('ending_type', models.CharField(max_length=5, null=True, choices=[(b'good', b'good'), (b'bad', b'bad'), (b'none', b'none')])),
                ('visits', models.IntegerField(default=0)),
                ('main_story_id', models.ForeignKey(to='zombies.Story')),
                ('parentSP', models.ForeignKey(to='zombies.StoryPoint', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(default=b'img/profile/tallahassee.jpg', upload_to=zombies.models.path_and_rename, blank=True)),
                ('exp', models.IntegerField(default=0)),
                ('finished_stories', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
