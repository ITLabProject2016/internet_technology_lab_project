from django.contrib import admin
from zombies.models import UserProfile, StoryPoint, Story  # , UserProfile_StoryPoint


class StoryPointAdmin(admin.ModelAdmin):
    list_display = (
        'main_story_id', 'story_point_id', 'parentSP', 'choiceText', 'description', 'experience', 'story_type')


# Registering models
admin.site.register(UserProfile)
admin.site.register(Story)
admin.site.register(StoryPoint, StoryPointAdmin)

# admin.site.register(UserProfile_StoryPoint)
