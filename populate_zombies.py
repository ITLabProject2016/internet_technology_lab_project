# We will most likely need a population script so that we can work with the same data.

# We have to import project's settings. When creating the script, uncomment the following lines first:
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zombies_on_campus.settings')

# These two lines import the Django settings. Uncomment these as well
# (otherwise will not allow to import our models)
import django

django.setup()

# Finally, uncomment and edit this line
from zombies.models import StoryPoint, Story


def populate():
    story = add_story(1, "zombies on campus", "stub description")

    # # Level 1
    sp1 = add_sp(None, 1, story, "You are in the library.", None, 10, "start")

    # Level 2
    sp2 = add_sp(sp1, 2, story, "You bump into your friend.", "Run.", 10, "mid")
    sp3 = add_sp(sp1, 3, story, "Zombie is friendly.", "Talk to zombie.", 10, "mid")

    # Level 3
    sp4 = add_sp(sp3, 4, story, "He's an asshole. You didn't like him.", "Talk more.", 10, "mid")
    sp5 = add_sp(sp3, 5, story, "You become very close.", "Shake hands.", 10, "mid")

    # Level 4
    sp6 = add_sp(sp4, 6, story, "You die.", "Punch him.", 10, "end")
    sp7 = add_sp(sp4, 7, story, "You become a zombie killer.", "Run away.", 10, "end")
    sp8 = add_sp(sp5, 8, story, "He catches you. You are forced into zombie marriage.",
                 "You are uncomfortable. Run away.", 10, "end")
    sp9 = add_sp(sp5, 9, story, "You get married. He decides you are too tasty not to eat you. Such is life (death?).",
                 "Your relationship continues.", 10, "end")


# sid - story_id; n - name; desc - description
def add_story(sid, n, desc):
    story = Story.objects.get_or_create(story_id=sid)[0]
    story.name = n
    story.description = desc
    story.save()
    return story


# Storypoint - story point which is the foreign key (which leads to this sp)
# s_id - story_id
# description - what the user will be shown AFTER selecting this story point
# choice - what the user will be shown BEFORE selecting this story point
# exp - how much experience points the user will get
# type - type of the story point (mid/end/start)
def add_sp(storypoint, s_id, mid, description, choice, exp, type):
    sp = StoryPoint.objects.get_or_create(parentSP=storypoint, story_point_id=s_id, main_story_id=mid)[0]
    # sp.story_id = s_id
    sp.description = description
    sp.choiceText = choice
    sp.experience = exp
    sp.story_type = type
    sp.save()
    return sp


if __name__ == '__main__':
    print "Starting Zombies population script..."
    populate()
