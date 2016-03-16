from django.contrib import admin
from zombies.models import UserProfile, StoryPoint, Story  # , UserProfile_StoryPoint
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import User


class StoryPointAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'main_story_id', 'parentSP', 'choiceText', 'description', 'picture', 'experience', 'story_type', 'ending_type', 'visits')


class StoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description', 'picture', 'visits')


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

# Registering models
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(Story, StoryAdmin)
admin.site.register(StoryPoint, StoryPointAdmin)

# admin.site.register(UserProfile_StoryPoint)
