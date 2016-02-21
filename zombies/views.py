from django.shortcuts import render


# This is the home page. Creates a view for it.
def home(request):
    # So far context dictionary is empty, but may be useful later
    context_dict = {'welcome_message' : "Hello! This will be our main page."}
    return render(request, 'zombies/home.html', context_dict)


# Links to about template. Any further logic should go here.
def about(request):
    context_dict = {'welcome_message' : "Hello! This will be our about page."}
    return render(request, 'zombies/about.html', context_dict)


# Links to profile template. Will probably have to do some serious logic with stats.
def profile(request):
    return render(request, 'zombies/profile.html', {})


# Links to login template.
def login(request):
    return render(request, 'zombies/login.html', {})


# Links to register template.
def register(request):
    return render(request, 'zombies/register.html', {})


# This will be our main view - will show the story points, etc.
def story(request):
    return render(request, 'zombies/story.html', {})


# This will be the address the user reaches after finishing the story.
# However, should it be different from story? Should we have a dynamic page
# instead, which should not be loaded - depending on which story point user is in,
# it simply changes to the end point. So this could be joined with story.
# Otherwise, once the player finishes the story, page will refresh, he/she will
# be taken to another address. Perhaps not very good?
def the_end(request):
    return render(request, 'zombies/the_end.html', {})


