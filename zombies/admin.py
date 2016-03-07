from django.contrib import admin
from zombies.models import UserProfile, StoryPoint, Story  # , UserProfile_StoryPoint


class StoryPointAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'main_story_id', 'parentSP', 'choiceText', 'description', 'experience', 'story_type', 'visits')


class StoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description', 'visits')


# Registering models
admin.site.register(UserProfile)
admin.site.register(Story, StoryAdmin)
admin.site.register(StoryPoint, StoryPointAdmin)

# admin.site.register(UserProfile_StoryPoint)
