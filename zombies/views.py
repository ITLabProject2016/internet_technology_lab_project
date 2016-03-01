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


# Links to login template.
def user_login(request):
    if request.method == 'POST':
        # Get username, password from the form.
        # If request.POST.get finds nothing, returns None. If request.POST used, raises key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        # If we have the correct details
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/zombies/')
            else:
                return HttpResponse("WE SHOULD CHANGE THIS TO THROW AN ERROR INSTEAD OF NEW PAGE")

        # Bad details provided
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("WE SHOULD CHANGE THIS TO THROW AN ERROR INSTEAD OF NEW PAGE")

    # If request.method is GET
    else:
        return render(request, 'zombies/login NOT USED.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/zombies/')


# Links to register template.
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Check if both forms are OK
        if user_form.is_valid() and profile_form.is_valid():
            # Save it to DB
            user = user_form.save()
            # set_password() hashes password
            user.set_password(user.password)
            user.save()

            userprofile = profile_form.save(commit=False)
            userprofile.user = user

            # If user provided a profile picture, get it from the input form, put in UserProfile model
            if 'picture' in request.FILES:
                userprofile.picture = request.FILES['picture']

            userprofile.save()

            # Everything went fine, so we set it to true
            registered = True

        # Some errors, invalid form, show them to user
        else:
            print user_form.errors, profile_form.errors

    # Request method = GET, so we show the form instead of collecting the data
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()


    return render(request, 'zombies/register NOT USED.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


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


