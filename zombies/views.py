from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from zombies.models import StoryPoint, Story
from django.contrib.auth.models import User
from itertools import cycle


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
    # Similar structure can be used to count other outcomes.
    if storytype == 'end':
        # If we do not make sure user is authenticated, the program hangs.
        if request.user.is_authenticated():
            user_profile.finished_stories += 1
            user_profile.save()

    # First our small_data
    # Problem: updated every time story point is visited. So for 3 steps, +3. Should be +1.
    # Do not write story.id = sid. What is passed from URL is ALWAYS a string. Need to cast to int.
    # warning a story should logged to be viewed only ONCE at the starting point
    if int(storypoint.id) == 1:
        story.visits += 1
        story.save()

    storypoint.visits += 1
    storypoint.save()

    choices = StoryPoint.objects.filter(main_story_id=story).filter(parentSP=storypoint)

    context_dict = {}
    context_dict['story'] = storypoint
    context_dict['choices'] = choices
    return render(request, 'zombies/story-point.html', context_dict)


# Simple global statistics about the game.
def statistics(request):
    # Get all storypoints
    spoints = StoryPoint.objects.all()


    story_ends = 0
    # If the story point has a type of ending, then it means it's a distinct story.
    for sp in spoints:
        if sp.story_type == 'end':
            story_ends += 1

    trees = len(Story.objects.all())
    users = len(User.objects.all())

    choices_made = 0
    storypoints = StoryPoint.objects.all()
    for storypoint in storypoints:
        # This method counts not only choices inside the story, but also the choice of the main story
        choices_made += storypoint.visits

    context_dict = {}
    context_dict['branches_count'] = story_ends
    context_dict['trees_count'] = trees
    context_dict['players'] = users
    context_dict['choices'] = choices_made

    #for the pie
    #the pie will demonstrate the preferences among the stories
    class Piece:
        def __init__(self):
            self.value = 20
            self.color = "#F7464A"
            self.highlight = "#FF5A5E"
            self.label = "story_part"

    colors = cycle(["#F7464A","#46BFBD","#FDB45C","#949FB1","#4D5360"])
    colorsh = cycle(["#FF5A5E","#5AD3D1","#FFC870","#A8B3C5","#616774"])

    pie = []
    stories = Story.objects.all()
    for s in stories:
        piece = Piece()
        piece.label = s.name
        piece.value = s.visits
        piece.color = next(colors)
        piece.highlight = next(colorsh)
        pie.append(piece)

    context_dict['pie'] = pie

    #for the bar now
    #the bar will show the visited good and bad endings for each story
    story_good_ends = [0]*len(Story.objects.all())
    story_bad_ends = [0]*len(Story.objects.all())

    for sp in spoints:
        if sp.story_type == 'end' and sp.ending_type=="good":
            story_good_ends[int(sp.main_story_id.id)-1] += sp.visits
        elif sp.story_type == 'end' and sp.ending_type=="bad":
            story_bad_ends[int(sp.main_story_id.id)-1] += sp.visits

    context_dict['story_good_ends'] = story_good_ends
    context_dict['story_bad_ends'] = story_bad_ends

    return render(request, 'zombies/statistics.html', context_dict)


# Experimental. Leaderboard: shows how many people have completed various things, who has completed the most, etc.
def survivors(request):

    context_dict = {}
    player_list = User.objects.all().order_by('-userprofile__exp')
    user_exp = []
    for player in player_list:
        username = player.username
        # Experience gained
        exp = player.userprofile.exp
        # Stories completed
        stories = player.userprofile.finished_stories
        user_exp.append([username, exp, stories])
    context_dict['user_info'] = user_exp

    return render(request, 'zombies/survivors.html', context_dict)
