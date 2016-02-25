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


