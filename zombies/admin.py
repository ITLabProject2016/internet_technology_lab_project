from django.contrib import admin
from zombies.models import UserProfile, StoryPoint #, UserProfile_StoryPoint


class StoryPointAdmin(admin.ModelAdmin):
    list_display = ('parentSP', 'story_id', 'choiceText', 'description', 'experience', 'story_type')


# Registering models
admin.site.register(UserProfile)
admin.site.register(StoryPoint, StoryPointAdmin)
# admin.site.register(UserProfile_StoryPoint)