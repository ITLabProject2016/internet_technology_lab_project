from django.contrib import admin
from zombies.models import UserProfile,StoryPoint,UserProfile_StoryPoint

# Registering models
admin.site.register(UserProfile)
admin.site.register(StoryPoint)
admin.site.register(UserProfile_StoryPoint)