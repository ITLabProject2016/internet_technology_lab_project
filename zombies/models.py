from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import os
from uuid import uuid4


# USEFUL INFO:
# Whenever changes to the models are made, need to register those changes like so:
#   python manage.py makemigrations <app_name>
# Then apply them like so:
#   python manage.py migrate

# To change password of a user (including admin):
#   manage.py changepassword <user_name>

# Don't forget to import/register models to admin.py
# http://www.tangowithdjango.com/book17/chapters/models.html#configuring-the-admin-interface
#
# for a good well-being please read
# https://docs.djangoproject.com/en/1.9/topics/db/models/

# Credit to: http://stackoverflow.com/questions/15140942/django-imagefield-change-file-name-on-upload
def path_and_rename(instance, filename):
    upload_to = 'img/profile'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class UserProfile(models.Model):
    # Link UserProfile with a User model instance
    user = models.OneToOneField(User)

    # User can choose a picture. Should not be necessary to upload it. Otherwise may be a bit annoying.
    # Images will be uploaded to /media/profile/ (unless we change it in settings.py).
    # DO NOT delete default link. If user chooses not to upload the picture, default will be given.
    picture = models.ImageField(upload_to=path_and_rename, blank=True, default="img/profile/tallahassee.jpg")
    # Calculate user's experience. Can add badges, give permissions, etc. based on that.
    exp = models.IntegerField(default=0)
    # Calculate how many stories user has finished.
    finished_stories = models.IntegerField(default=0)

    # Return username when object is printed
    def __unicode__(self):
        return self.user.username


# Allows us to populate the user with additional fields.
# Links UserProfile with User.
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)


class Story(models.Model):
    #story_id = models.IntegerField(max_length=6, unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to='img/story', blank=True, default=None)
    visits = models.IntegerField(default=0)

    # Corrects "Story" to "Stories"
    class Meta:
        verbose_name_plural = "Stories"

    def __unicode__(self):
        return str(self.id)


# Explanation of changes: title - not sure if needed, so deleted. Photo - commented out.
# Need to use ImageField (https://docs.djangoproject.com/en/1.7/ref/models/fields/#filefield)
# Others: renamed for clarity, reduced max length (stories have to bo short).
# Added experience - so that user can get experience depending on how well he/she does.
# story_type - whether beginning, mid or end.
class StoryPoint(models.Model):
    #story_point_id = models.IntegerField(max_length=6, unique=True)
    #we dont need ids because django creates them by default
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

    parentSP = models.ForeignKey('self', null=True)
    main_story_id = models.ForeignKey(Story)
    story_point_id = models.IntegerField(default=0)
    description = models.CharField(max_length=1000, blank=False, null=False)
    picture = models.ImageField(upload_to='img/story_point', blank=True, default=None)
    choiceText = models.CharField(max_length=100, blank=True, null=True)
    experience = models.IntegerField(default=0)
    story_type = models.CharField(max_length=5, choices=STORY_TYPES, blank=False, null=False)
    ending_type = models.CharField(max_length=5, choices=STORY_END, blank=False, null=True)
    visits = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id)

    def __to_string__(self):
        Str = 'story point obj: ' + str(self.main_story_id) +' '+str(self.story_point_id) +' '+ str(self.description)+' '+ str(self.story_type)
        return str(Str)

# Not too sure if this model is needed - we should be able to do everything with UserProfile.
# Might need to ask Leif whether we need to create more models for stats.
# class UserProfile_StoryPoint(models.Model):
#     user = models.ForeignKey(UserProfile)
#     storypoint = models.ForeignKey(StoryPoint   )
#
#     def __unicode__(self):
#         return self.storypoint.title
