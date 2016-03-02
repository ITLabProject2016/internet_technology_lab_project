from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from zombies.forms import UserForm, UserProfileForm


# This is the home page. Creates a view for it.
def home(request):
    # So far context dictionary is empty, but may be useful later
    # Dictionaries are constructed by specifying key and then value {key:value}.
    # Key is used in templates, using Django template language. Value is what's actually shown.
    context_dict = {'welcome_message': "Hello! This will be our main page."}
    return render(request, 'zombies/home.html', context_dict)


# Links to about template. Any further logic should go here.
def about(request):
    context_dict = {'welcome_message' : "Hello! This will be our about page."}
    return render(request, 'zombies/about.html', context_dict)


# Links to profile template. Will probably have to do some serious logic with stats.
# Also, not too sure about the decorator - profile view should not be shown if you're not logged in.
# But is the decorator the best way to achieve it?
@login_required
def profile(request):
    return render(request, 'zombies/profile.html', {})


# This will be our main view - will show the story points, etc.
def story(request):
    return render(request, 'zombies/story.html', {})


def story_change(request):
    # get user's cookie
    context_dict = {'description': "This is one story description loaded directly from views.py!!!!"}
    return render(request, 'zombies/story_part.html', context_dict)

# This will be the address the user reaches after finishing the story.
# However, should it be different from story? Should we have a dynamic page
# instead, which should not be loaded - depending on which story point user is in,
# it simply changes to the end point. So this could be joined with story.
# Otherwise, once the player finishes the story, page will refresh, he/she will
# be taken to another address. Perhaps not very good?
def the_end(request):
    return render(request, 'zombies/the_end.html', {})


