# We will most likely need a population script so that we can work with the same data.

# We have to import project's settings. When creating the script, uncomment the following lines first:
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zombies_on_campus.settings')

# These two lines import the Django settings. Uncomment these as well
# (otherwise will not allow to import our models)
import django

django.setup()

# Finally, uncomment and edit this line
from zombies.models import Story, StoryPoint


def populate():
    #the story name has to be unique
    story = add_story("zombies on sir alan williams", "stub description hahahaha")

    # # Level 1
    sp1 = add_sp(story, None,  "You are in the library.", None, 10, "start")

    # Level 2
    sp2 = add_sp(story, sp1,  "You bump into your friend.", "Run.", 10, "mid")
    sp3 = add_sp(story, sp1,  "Zombie is friendly.", "Talk to zombie.", 10, "mid")

    # Level 3
    sp4 = add_sp(story, sp3,  "He's an asshole. You didn't like him.", "Talk more.", 10, "mid")
    sp5 = add_sp(story, sp3, "You become very close.", "Shake hands.", 10, "mid")

    # Level 4
    sp6 = add_sp(story, sp4,  "You die.", "Punch him.", 10, "end")
    sp7 = add_sp(story, sp4,  "You become a zombie killer.", "Run away.", 10, "end")

    #Level 5
    sp8 = add_sp(story, sp5,  "He catches you. You are forced into zombie marriage.",
                 "You are uncomfortable. Run away.", 10, "end")
    sp9 = add_sp(story, sp5,  "You get married. He decides you are too tasty not to eat you. Such is life (death?).",
                 "Your relationship continues.", 10, "end")


# sid - story_id; n - name; desc - description
def add_story(n, desc):
    story = Story.objects.create(name=n, description = desc)
    return story

# Storypoint - story point which is the foreign key (which leads to this sp)
# s_id - story_id
# description - what the user will be shown AFTER selecting this story point
# choice - what the user will be shown BEFORE selecting this story point
# exp - how much experience points the user will get
# type - type of the story point (mid/end/start)
def add_sp(mid, storypoint_parent, desc, choice, exp, type):
    sp = StoryPoint.objects.create(
        main_story_id=mid,
        parentSP=storypoint_parent,
        description = desc,
        choiceText = choice,
        experience = exp,
        story_type = type)

    return sp


if __name__ == '__main__':
    print "Starting Zombies population script..."
    populate()
