from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from zombies.models import StoryPoint, Story
from django.contrib.auth.models import User



# This is the home page.
# We now list stories
def index(request):
    story_list = Story.objects.order_by('id')
    context_dict = {'stories': story_list}
    return render(request, 'zombies/index.html', context_dict)


def index_min(request):
    story_list = Story.objects.order_by('id')
    context_dict = {'stories': story_list}
    return render(request, 'zombies/index_min.html', context_dict)


# Links to about template. Any further logic should go here.
def about(request):
    return render(request, 'zombies/about.html', {})


# Links to profile template.
# Not too sure about the decorator - profile view should not be shown if you're not logged in.
# But is the decorator the best way to achieve it?
@login_required
def profile(request):
    return render(request, 'zombies/profile.html', {})


def story_point(request, sid, spid):
    storyID = int(sid)
    storypointID = int(spid)
    story = Story.objects.get(id=sid)

    storypoint = StoryPoint.objects.filter(main_story_id=story).get(story_point_id=storypointID)

    # First our small_data
    # Problem: updated every time story point is visited. So for 3 steps, +3. Should be +1.
    # Do not write story.id = sid. What is passed from URL is ALWAYS a string. Need to cast to int.
    if story.id == int(sid):
        story.visits += 1
        story.save()
    storypoint.visits += 1
    storypoint.save()

    choices = StoryPoint.objects.filter(main_story_id=story).filter(parentSP=storypoint)

    context_dict = {}
    context_dict['story'] = storypoint
    context_dict['choices'] = choices
    return render(request, 'zombies/story-point.html', context_dict)
    #return HttpResponse(storypoint.__to_string__())


# Simple global statistics about the game.
def statistics(request):
    # Get the relevant
    branches = len(StoryPoint.objects.all())
    trees = len(Story.objects.all())
    users = len(User.objects.all())

    choices_made = 0
    storypoints = StoryPoint.objects.all()
    for storypoint in storypoints:
        # This method counts not only choices inside the story, but also the choice of the main story
        choices_made += storypoint.visits

    context_dict = {}
    context_dict['branches_count'] = branches
    context_dict['trees_count'] = trees
    context_dict['players'] = users
    context_dict['choices'] = choices_made
    return render(request, 'zombies/statistics.html', context_dict)