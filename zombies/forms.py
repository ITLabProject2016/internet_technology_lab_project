from django import forms
from zombies.models import UserProfile


# To allow the user to upload a profile picture
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
