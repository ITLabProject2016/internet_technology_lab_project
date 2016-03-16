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
    file = open("./populate/dev.jpg")
    dJango_file = File(file, 'r')
    name = os.path.basename(file)
    print name
    sp.picture.save(name, dJango_file)
    sp.save()


