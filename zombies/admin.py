from django.contrib import admin
from zombies.models import UserProfile, StoryPoint #, UserProfile_StoryPoint


class StoryPointAdmin(admin.ModelAdmin):
    list_display = ('story_id', 'parentSP', 'choiceText', 'description', 'experience', 'story_type')


# Registering models
admin.site.register(UserProfile)
admin.site.register(StoryPoint, StoryPointAdmin)
# admin.site.register(UserProfile_StoryPoint)