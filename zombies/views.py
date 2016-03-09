from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from zombies.models import StoryPoint, Story
from django.contrib.auth.models import User


# Home page. At the moment, we list all the stories. Should we not present a random one instead?
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


# Links to profile template. Profile view should not be shown if you're not logged in.
@login_required
def profile(request):
    username = request.user.username
    user_profile = request.user.userprofile
    experience = user_profile.exp
    # This is more of a placeholder. We can collect stats such as: deaths, marriages, heroic deeds, etc.
    # Depends on our creativity and how much we're willing to tinker with it.
    finished = user_profile.finished_stories
    context_dict = {}
    context_dict['username'] = username
    context_dict['experience'] = experience
    context_dict['finished_stories'] = finished
    return render(request, 'zombies/profile.html', context_dict)


# Links to the story_point template. Main stats are collected here.
def story_point(request, sid, spid):
    storyID = int(sid)
    storypointID = int(spid)
    story = Story.objects.get(id=sid)

    storypoint = StoryPoint.objects.filter(main_story_id=story).get(story_point_id=storypointID)

    # Adds experience to the currently logged in user
    # If the user is not logged in, skips it
    # We can play around with experience points (e.g. ending without death gives more)
    if request.user.is_authenticated():
        user_profile = request.user.userprofile
        user_profile.exp += storypoint.experience
        user_profile.save()

    storytype = storypoint.story_type
    print storytype
    if storytype == 'end':
        user_profile.finished_stories += 1
        user_profile.save()


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
    # Get all storypoints
    spoints = StoryPoint.objects.all()
    stories = 0
    # If the story point has a type of ending, then it means it's a distinct story.
    for sp in spoints:
        if sp.story_type == 'end':
            stories += 1

    trees = len(Story.objects.all())
    users = len(User.objects.all())

    choices_made = 0
    storypoints = StoryPoint.objects.all()
    for storypoint in storypoints:
        # This method counts not only choices inside the story, but also the choice of the main story
        choices_made += storypoint.visits

    context_dict = {}
    context_dict['branches_count'] = stories
    context_dict['trees_count'] = trees
    context_dict['players'] = users
    context_dict['choices'] = choices_made
    return render(request, 'zombies/statistics.html', context_dict)