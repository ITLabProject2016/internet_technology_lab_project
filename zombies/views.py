from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from zombies.models import StoryPoint, Story
from random import randrange



# This is the home page.
def home(request):
    context_dict = {'welcome_message': "Hello! This will be our main page."}
    return render(request, 'zombies/home.html', context_dict)


# Links to about template. Any further logic should go here.
def about(request):
    context_dict = {'welcome_message' : "Hello! This will be our about page."}
    return render(request, 'zombies/about.html', context_dict)


# Links to profile template.
# Not too sure about the decorator - profile view should not be shown if you're not logged in.
# But is the decorator the best way to achieve it?
@login_required
def profile(request):
    return render(request, 'zombies/profile.html', {})


# Links with story_change in JS. So that the URL never changes and is always story url
def story(request):
    return render(request, 'zombies/story.html', {})


def story_change(request):
    # we need to get user's cookie

    # Get how many stories we have (if we have more than one, we can randomize them)
    # Since we only have one story now, it will generate a random nr between 1 and 1 (1)
    # Perhaps this should go into story view, though, since we only pick the story once (each time play is pressed)?
    story_count = len(Story.objects.all())
    random_story = randrange(1, story_count + 1)  # means [1-story_count] (inclusive)
    # This line is used to get all the storypoints that are connected to a particular story.
    # At the moment, it picks random story from all available stories (so we don't show all available ones).
    # Thus the game is more unpredictable and interesting (in my opinion -Simonas)
    # However, we should probably do it once somehow, because at the moment, we're doing it every time view is called
    # (at least I think so)
    storypoint_list = StoryPoint.objects.filter(main_story_id=random_story)
    # What I didn't manage to do (we probably need cookies for that - to track when we already called first point):
    # Get the first story point, and then iterate over its children, each time getting different story points
    # (e.g., if you click on sp1, you get story points connected to it, then story points to those before and so on)

    # First story point - where everything begins. Pick from the stories we got through randomization/filtering
    story = storypoint_list.order_by('story_point_id')[0]

    choices = StoryPoint.objects.filter(parentSP=story)
    context_dict = {'description': "This is one story description loaded directly from views.py!!!!",
                    'storypoints': storypoint_list,
                    'count': story_count,
                    'random_story': random_story,
                    'test': story,
                    'choices': choices}
    return render(request, 'zombies/story_part.html', context_dict)


# This is probably not needed anymore
def the_end(request):
    return render(request, 'zombies/the_end.html', {})


# Two methods below are for testing only:
# seeing whether it is possible to make it work with simple links
def storytest(request):
    story_count = len(Story.objects.all())
    random_story = randrange(1, story_count + 1)
    storypoint_list = StoryPoint.objects.filter(main_story_id=random_story)
    story = storypoint_list.order_by('story_point_id')[0]
    choices = StoryPoint.objects.filter(parentSP=story)

    context_dict = {'choices': choices, 'beginning': story}

    return render(request, 'zombies/sptest.html', context_dict)


def sp(request, spid):
    storypointID = int(spid)
    storypoint = StoryPoint.objects.filter(story_point_id=storypointID)[0]
    choices = StoryPoint.objects.filter(parentSP=storypoint)

    descr = storypoint.description

    context_dict = {}
    context_dict['story'] = storypoint
    context_dict['choices'] = choices
    return render(request, 'zombies/sp.html', context_dict)
