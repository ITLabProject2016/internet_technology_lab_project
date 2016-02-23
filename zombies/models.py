from django.db import models

# USEFUL INFO:
# Whenever changes to the models are made, need to register those changes like so:
#   python manage.py makemigrations <app_name>
# Then apply them like so:
#   python manage.py migrate

# To change password of a user (including admin):
#   manage.py changepassword <user_name>

# Don't forget to import/register models to admin.py
# http://www.tangowithdjango.com/book17/chapters/models.html#configuring-the-admin-interface