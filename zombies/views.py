from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from zombies.models import StoryPoint, Story
from random import randrange

# This is the home page.
def index(request):

    story_list = Story.objects.order_by('story_id')[:4]
    context_dict = {'stories': story_list}
    return render(request, 'zombies/index.html', context_dict)

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
def story_point(request, spid):
    storypointID = int(spid)
    storypoint = StoryPoint.objects.filter(story_point_id=storypointID)[0]
    choices = StoryPoint.objects.filter(parentSP=storypoint)

    descr = storypoint.description

    context_dict = {}
    context_dict['story'] = storypoint
    context_dict['choices'] = choices
    return render(request, 'zombies/story-point.html', context_dict)


# def story_change(request):
#     # we need to get user's cookie
#
#     # Get how many stories we have (if we have more than one, we can randomize them)
#     # Since we only have one story now, it will generate a random nr between 1 and 1 (1)
#     # Perhaps this should go into story view, though, since we only pick the story once (each time play is pressed)?
#     story_count = len(Story.objects.all())
#     random_story = randrange(1, story_count + 1)  # means [1-story_count] (inclusive)
#     # This line is used to get all the storypoints that are connected to a particular story.
#     # At the moment, it picks random story from all available stories (so we don't show all available ones).
#     # Thus the game is more unpredictable and interesting (in my opinion -Simonas)
#     # However, we should probably do it once somehow, because at the moment, we're doing it every time view is called
#     # (at least I think so)
#     storypoint_list = StoryPoint.objects.filter(main_story_id=random_story)
#     # What I didn't manage to do (we probably need cookies for that - to track when we already called first point):
#     # Get the first story point, and then iterate over its children, each time getting different story points
#     # (e.g., if you click on sp1, you get story points connected to it, then story points to those before and so on)
#
#     # First story point - where everything begins. Pick from the stories we got through randomization/filtering
#     story = storypoint_list.order_by('story_point_id')[0]
#
#     choices = StoryPoint.objects.filter(parentSP=story)
#     context_dict = {'description': "This is one story description loaded directly from views.py!!!!",
#                     'storypoints': storypoint_list,
#                     'count': story_count,
#                     'random_story': random_story,
#                     'test': story,
#                     'choices': choices}
#     return render(request, 'zombies/###.html', context_dict)



