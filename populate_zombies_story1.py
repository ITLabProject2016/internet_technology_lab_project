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


def populate():
    #the story name has to be unique
    story = add_story("Zombies on Campus", "Stub description.", "dev")

    # # Level 1
    sp1 = add_sp(story, 1, None,  "You are in the library.", "dev", None, 10, "start", None)

    # Level 2
    sp2 = add_sp(story, 2, sp1,  "You bump into your friend.", "dev", "Run.", 10, "mid", None)
    sp3 = add_sp(story, 3, sp1,  "Zombie is friendly.", "dev", "Talk to zombie.", 10, "mid", None)

    # Level 3
    sp4 = add_sp(story, 4, sp3,  "He's an asshole. You didn't like him.", "dev", "Talk more.", 10, "mid", None)
    sp5 = add_sp(story, 5, sp3, "You become very close.", "dev", "Shake hands.", 10, "mid", None)

    # Level 4
    sp6 = add_sp(story, 6, sp4,  "You die.", "dev", "Punch him.", 10, "end", "good")
    sp7 = add_sp(story, 7, sp4,  "You become a zombie killer.", "dev", "Run away.", 10, "end", "bad")

    #Level 5
    sp8 = add_sp(story, 8, sp5,  "He catches you. You are forced into zombie marriage.", "dev",
                 "You are uncomfortable. Run away.", 10, "end", "good")
    sp9 = add_sp(story, 9, sp5,  "You get married. He decides you are too tasty not to eat you. Such is life (death?).", "dev",
                 "Your relationship continues.", 10, "end", "good")


# sid - story_id; n - name; desc - description
def add_story(n, desc, pic):

    path = "./populate_img/"+pic+".jpg"
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

    path = "./populate_img/"+pic+".jpg"
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


if __name__ == '__main__':
    print "Starting Zombies population script..."
    populate()
