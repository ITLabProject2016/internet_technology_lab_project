from django.db import models
from django.contrib.auth.models import User


# USEFUL INFO:
# Whenever changes to the models are made, need to register those changes like so:
#   python manage.py makemigrations <app_name>
# Then apply them like so:
#   python manage.py migrate

# To change password of a user (including admin):
#   manage.py changepassword <user_name>

# Don't forget to import/register models to admin.py
# http://www.tangowithdjango.com/book17/chapters/models.html#configuring-the-admin-interface


class UserProfile(models.Model):
    # Link UserProfile with a User model instance
    user = models.OneToOneField(User)

    # User can choose a picture. Should not be necessary to upload it. Otherwise may be a bit annoying.
    # Images will be uploaded to /media/profile_images/ (unless we change it in settings.py).
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Return username when object is printed
    def __unicode__(self):
        return self.user.username


class Story(models.Model):
    story_id = models.IntegerField(max_length=6, unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)

    # Corrects "Story" to "Stories"
    class Meta:
        verbose_name_plural = "Stories"

    def __unicode__(self):
        return str(self.story_id)


# Explanation of changes: title - not sure if needed, so deleted. Photo - commented out.
# Need to use ImageField (https://docs.djangoproject.com/en/1.7/ref/models/fields/#filefield)
# Others: renamed for clarity, reduced max length (stories have to bo short).
# Added experience - so that user can get experience depending on how well he/she does.
# story_type - whether beginning, mid or end.
class StoryPoint(models.Model):
    story_point_id = models.IntegerField(max_length=6, unique=True)
    parentSP = models.ForeignKey('self', null=True)
    main_story_id = models.ForeignKey(Story)
    description = models.CharField(max_length=1000, blank=False, null=False)
    choiceText = models.CharField(max_length=100, blank=True, null=True)
    experience = models.IntegerField(default=0)
    story_type = models.CharField(max_length=5, default='mid', blank=False, null=False)

    def __unicode__(self):
        return str(self.story_point_id)

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
