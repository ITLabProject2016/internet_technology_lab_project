__author__ = 'kostis'

import os
import Image

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zombies_on_campus.settings')

import django

django.setup()

from django.core.files import File
from zombies.models import StoryPoint, Story

storypoints = StoryPoint.objects.all()
for sp in storypoints:
    file = open("./populate/diff.png")
    dJango_file = File(file, 'r')
    name = "picture.png"
    sp.picture.save(name, dJango_file)
    sp.save()


