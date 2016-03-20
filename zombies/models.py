from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import os
from uuid import uuid4


# Helper function to rename the file upon uploading it.
# Credit to: http://stackoverflow.com/questions/15140942/django-imagefield-change-file-name-on-upload
def path_and_rename(instance, filename):
    upload_to = 'img/profile'
    # Gets image's extension.
    extension = filename.split('.')[-1]
    # Gets image's filename.
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, extension)
    else:
        # Set the filename to a random string
        filename = '{}.{}'.format(uuid4().hex, extension)
    return os.path.join(upload_to, filename)


# Additional fields for User model are defined here.
class UserProfile(models.Model):
    # Links UserProfile with a User model instance
    user = models.OneToOneField(User)

    # User can choose a picture. Images are uploaded to /media/img/profile/.
    # If a user chooses not to upload a picture, default picture will be given to him/her.
    picture = models.ImageField(upload_to=path_and_rename, blank=True, default="img/profile/tallahassee.jpg")
    # Calculates user's experience. Depending on it, user earns badges and so on.
    exp = models.IntegerField(default=0)
    # Calculates how many stories user has finished.
    finished_stories = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username


# Allows us to populate the user with additional fields. Links UserProfile with a User instance.
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)


# Main story to which story points are connected.
class Story(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to='img/story', blank=True, default=None)
    # How many times this particular story has been picked by the users.
    visits = models.IntegerField(default=0)

    # Corrects "Story" to "Stories"
    class Meta:
        verbose_name_plural = "Stories"

    def __unicode__(self):
        return str(self.id)


# 'Meat' of a story. User proceeds from one story point to the other. The path depends on which choice text is chosen.
# Each story point has a unique description, some statistical information and so on.
class StoryPoint(models.Model):
    STORY_TYPES = (
        ('start', 'start'),
        ('mid', 'mid'),
        ('end', 'end'),
    )

    STORY_END = (
        ('good', 'good'),
        ('bad', 'bad'),
        ('none', 'none'),
    )

    # Which main story line a particular story point is connected to.
    main_story_id = models.ForeignKey(Story)
    # Which story point leads to a current story point.
    parentSP = models.ForeignKey('self', null=True)
    # Current SP's ID.
    story_point_id = models.IntegerField(default=0)
    description = models.CharField(max_length=1000, blank=False, null=False)
    picture = models.ImageField(upload_to='img/story_point', blank=True, default=None)
    choiceText = models.CharField(max_length=100, blank=True, null=True)
    experience = models.IntegerField(default=0)
    story_type = models.CharField(max_length=5, choices=STORY_TYPES, blank=False, null=False)
    ending_type = models.CharField(max_length=5, choices=STORY_END, blank=False, null=True)
    # How many times this particular SP has been picked by the users.
    visits = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id)

    def __to_string__(self):
        Str = 'story point obj: ' + str(self.main_story_id) + ' ' + str(self.story_point_id) + ' ' + str(
            self.description) + ' ' + str(self.story_type)
        return str(Str)
