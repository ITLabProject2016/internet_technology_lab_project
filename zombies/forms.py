# ModelForm - helper class that allows to create Django forms from a pre-existing model.

from django import forms
from django.contrib.auth.models import User
from zombies.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    # Additional properties about this ModelForm class
    class Meta:
        model = User
        # What we want to be presented in the form
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


