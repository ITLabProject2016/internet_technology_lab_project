from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from zombies.models import StoryPoint, Story
from random import randrange


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


# Takes number passed through URL, matches with the corresponding storypoint (lets call it SP).
# Then, gets the story points that have SP as their foreign key. In templates, shows the choice text.
# Links in template lead to the choice's story part (again, by passing the story+_point_id (spid)).
# Problems with this approach: URL changes every time you click on a story point.
# Story points can be accessed by simply entering the URL.
# Can we make something similar, but with JS, as we have now when we click play? Can we pass
# context dictionary to JS files? If we can, we could do similar logic and make it work, perhaps.
# If not, we need to:
# 1. Figure out what main story to pick, get the first story point, present choices.
# 2. Change choice text/description/picture according to the choice selected (just as we have now).
# 3. Figure out how to pass values associated with choices to the view.
def story_point(request, sid, spid):
    storyID = int(sid)
    storypointID = int(spid)
    print storyID
    print storypointID
    story = Story.objects.get(id=sid)

    storypoint = StoryPoint.objects.filter(main_story_id = story).get(story_point_id = storypointID)

    #first our small_data
    if storypoint == 1:
        story.visits = story.visits + 1
        story.save()
    storypoint.visits = storypoint.visits + 1
    storypoint.save()

    choices = StoryPoint.objects.filter(main_story_id=story).filter(parentSP=storypoint)
    descr = storypoint.description

    context_dict = {}
    context_dict['story'] = storypoint
    context_dict['choices'] = choices
    return render(request, 'zombies/story-point.html', context_dict)
    #return HttpResponse(storypoint.__to_string__())