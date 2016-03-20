# We will most likely need a population script so that we can work with the same data.
# We have to import project's settings. When creating the script, uncomment the following lines first:
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zombies_on_campus.settings')

# These two lines import the Django settings. Uncomment these as well
# (otherwise will not allow to import our models)
import django

django.setup()

# Finally, uncomment and edit this line
from django.core.files import File
from zombies.models import Story, StoryPoint


# sid - story_id; n - name; desc - description
def add_story(n, desc, pic):

    path = "populate_img/stories/"+pic+".jpg"
    dJango_file = File(open(path), 'r')
    name = os.path.basename(path)

    story = Story.objects.create(name=n, description = desc)

    story.picture.save(name, dJango_file)
    story.save()

    return story

# Storypoint - story point which is the foreign key (which leads to this sp)
# s_id - story_id
# description - what the user will be shown AFTER selecting this story point
# choice - what the user will be shown BEFORE selecting this story point
# exp - how much experience points the user will get
# type - type of the story point (mid/end/start)
def add_sp(mid, sid,storypoint_parent, desc, pic, choice, exp, type, end):

    path = "populate_img/points/"+pic+".jpg"
    dJango_file = File(open(path), 'r')
    name = os.path.basename(path)

    sp = StoryPoint.objects.create(
        main_story_id=mid,
        story_point_id = sid,
        parentSP=storypoint_parent,
        description = desc,
        choiceText = choice,
        experience = exp,
        story_type = type,
        ending_type = end,
    )

    sp.picture.save(name, dJango_file)
    sp.save()

    return sp

