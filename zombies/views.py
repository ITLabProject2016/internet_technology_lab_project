from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from zombies.models import StoryPoint, Story
from django.contrib.auth.models import User
from itertools import cycle
from zombies.forms import UserProfileForm


# Home page. The very first page people see upon entering the website.
def index(request):
    story_list = Story.objects.order_by('id')
    context_dict = {'stories': story_list}
    # Clears the cookies. Otherwise if the exits the story before finishing it, the cookie will persist and the
    # 'Story so far' will list all the story points visited before the session was abruptly ended.
    request.session['progression'] = ""

    return render(request, 'zombies/index.html', context_dict)


# This is shown by AJAX so that the URL does not change.
def index_min(request):
    story_list = Story.objects.order_by('id')
    context_dict = {'stories': story_list}

    return render(request, 'zombies/index_min.html', context_dict)


# 'About' view.
def about(request):
    return render(request, 'zombies/about.html', {})


# Links to profile template. Has a form inside it that allows users to upload a profile image.
# Also, provides some personal statistics.
@login_required
def profile(request):
    # Since most of the interesting fields are in user profile, get it at the very beginning (will be used in any case).
    user_profile = request.user.userprofile

    if request.method == 'POST':
        # Create user form
        picture_form = UserProfileForm(request.POST, request.FILES)
        # Checks if it's valid. If it is, clean up the picture, save it to DB.
        if picture_form.is_valid():
            picture = picture_form.cleaned_data['picture']
            user_profile.picture = picture
            user_profile.save()
            # Simply shows the profile again, so that the user sees the updated profile picture.
            return HttpResponseRedirect('/zombies/profile')
    # Method was GET, thus presents the form.
    else:
        picture_form = UserProfileForm()

    username = request.user.username
    experience = user_profile.exp
    # Path to a profile image
    picture = user_profile.picture.url
    # How many stories the user has finished
    finished = user_profile.finished_stories

    # Passes everything retrieved from DB to the context dictionary.
    context_dict = {}
    context_dict['username'] = username
    context_dict['picture'] = picture
    context_dict['experience'] = experience
    context_dict['finished_stories'] = finished
    context_dict['picture_form'] = picture_form

    return render(request, 'zombies/profile.html', context_dict)


# Shows how many people have completed various things, who has completed the most, etc.
# Orders the players according to their experience gained.
def survivors(request):
    context_dict = {}
    # Get all registered users and order them by experience
    player_list = User.objects.all().order_by('-userprofile__exp')
    # Initiate a list of user experiences
    user_info = []
    # Iterate over all players
    for player in player_list:
        # Get player's username
        username = player.username
        # Get their experience
        exp = player.userprofile.exp
        # Get how many stories they have completed
        stories = player.userprofile.finished_stories
        # Add them all to a list as another list (so that it can be used in template with ease)
        user_info.append([username, exp, stories])
    context_dict['user_info'] = user_info

    return render(request, 'zombies/survivors.html', context_dict)


# Profiles of other players. Similar to player profile, however, one cannot change anything in it.
def survivor_profile(request, username):
    context_dict = {}
    # Get survivor according to the username that was passed
    survivor = User.objects.get(username=username)
    # Get all relevant information
    survivor_prof = survivor.userprofile
    picture = survivor_prof.picture.url
    exp = survivor_prof.exp
    finished_stories = survivor_prof.finished_stories

    # Add everything to context dictionary
    context_dict['username'] = username
    context_dict['picture'] = picture
    context_dict['experience'] = exp
    context_dict['finished_stories'] = finished_stories

    return render(request, 'zombies/survivor_profile.html', context_dict)


# This is the corner stone of the whole application. Deals with connecting the stories, passing right
# variables to the templates, making sure that the choice text corresponds with the right story point, etc.
# Main stats are collected here, as well as the story progression text.
def story_point(request, sid, spid):
    storypoint_id = int(spid)
    story = Story.objects.get(id=sid)

    storypoint = StoryPoint.objects.filter(main_story_id=story).get(story_point_id=storypoint_id)

    # Adds experience to the currently logged in user. If the user is not logged in, skips it.
    # Also, increments finished stories if the user has reached the end of a particular story line.
    storytype = storypoint.story_type
    if request.user.is_authenticated():
        user_profile = request.user.userprofile
        user_profile.exp += storypoint.experience
        if storytype == 'end':
            user_profile.finished_stories += 1
        user_profile.save()

    # If it is the first story point in a particular story line, it means that story line has been visited.
    # Increments visits.
    if int(storypoint.story_point_id) == 1:
        story.visits += 1
        story.save()
    # Every time this view is called, it means that the story point has been clicked. Increments visits.
    storypoint.visits += 1
    storypoint.save()

    # Get all choices that are available to the user (depends on the current story point).
    # Choices are those story parts that have current story part as their foreign key.
    choices = StoryPoint.objects.filter(main_story_id=story).filter(parentSP=storypoint)

    # Request a cookie and put its value in a temp variable.
    progression = request.session.get('progression')
    # If cookie is empty, it means it should be the description of first story point
    # (if it was not first, it would not be empty).
    if not progression:
        progression = [storypoint.description]
    # If it is not empty, it means there already is some description inside it, so it only needs to add on to it.
    else:
        progression = progression + [storypoint.description]
    # Put it back in the cookie
    request.session['progression'] = progression
    # Clear the cookies if the user has finished a story (end point has no other SPs associated with it)
    if not choices:
        request.session['progression'] = [' ']

    context_dict = {}
    context_dict['progression'] = progression
    context_dict['story'] = storypoint
    context_dict['choices'] = choices

    return render(request, 'zombies/story-point.html', context_dict)


# Global statistics about the game, as well as the code for pie charts and bar charts.
def statistics(request):
    # Gets all story points. They are used to calculate global stats.
    story_points = StoryPoint.objects.all()

    # Calculate original stories. If the story point has a type of 'end', then it means it's a distinct story line.
    story_ends = 0
    for sp in story_points:
        if sp.story_type == 'end':
            story_ends += 1

    # How many main stories & users we have.
    trees = len(Story.objects.all())
    users = len(User.objects.all())

    # How many choices have been made in total.
    choices_made = 0
    for sp in story_points:
        choices_made += sp.visits

    context_dict = {}
    context_dict['branches_count'] = story_ends
    context_dict['trees_count'] = trees
    context_dict['players'] = users
    context_dict['choices'] = choices_made

    # Pie chart. Demonstrates the preferences among the stories.
    # Class that is responsible for a piece of pie.
    class Piece:
        def __init__(self):
            self.value = 20
            self.color = "#F7464A"
            self.highlight = "#FF5A5E"
            self.label = "story_part"

    colors = cycle(["#F7464A", "#46BFBD", "#FDB45C", "#949FB1", "#4D5360"])
    colorsh = cycle(["#FF5A5E", "#5AD3D1", "#FFC870", "#A8B3C5", "#616774"])

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

    # Bar chart. Shows visited good and bad endings for each story.
    story_good_ends = [0] * len(Story.objects.all())
    story_bad_ends = [0] * len(Story.objects.all())

    for sp in story_points:
        if sp.story_type == 'end' and sp.ending_type == "good":
            story_good_ends[int(sp.main_story_id.id) - 1] += sp.visits
        elif sp.story_type == 'end' and sp.ending_type == "bad":
            story_bad_ends[int(sp.main_story_id.id) - 1] += sp.visits

    context_dict['story_good_ends'] = story_good_ends
    context_dict['story_bad_ends'] = story_bad_ends

    return render(request, 'zombies/statistics.html', context_dict)
