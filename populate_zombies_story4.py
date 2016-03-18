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
    story = add_story("Love Story in Campus", " Wonderful days were those", "dev")

    # # Level 1
    sp1 = add_sp(story, 1, None,  "Your first day in Uni and heart broken as just been dumped, but came with the hope and desire to explore something new and exciting.", "dev", None, 10, "start", None)

    # Level 2
    sp2 = add_sp(story, 2, sp1,  "You see a bunch of folks, on left there's a gang of hot girls and on your right there's a gang of sexy boys. ",  "dev", "Go to the cafe",10, "mid", None)
    sp3 = add_sp(story, 3, sp1,  "O no! you missed the party, all your friends were enjoying in that cave. Awesome!!", "dev", "Go to the registration office", 10, "end", None)

    # Level 3
    sp4 = add_sp(story, 4, sp2,  "Nah! the girls were not intersted, didn't entertain you. ", "dev", "Go to the left", 10, "mid", "bad")
    sp5 = add_sp(story, 5, sp2,  "Ooh la la! all boys are drooling to see you.", "dev", "Go to the right", 10, "mid", None)
    sp6 = add_sp(story, 6, sp2,  "No chance for you, you actually are pretty boring.", "dev", "Neither left or right. Just stright ahead.", 10, "end", "bad")

    #Level 4
    sp7 = add_sp(story, 7, sp4,  "", "dev", "Simply disheartened, and go to your lectures.", 10, "mid", None)
    sp8 = add_sp(story, 8, sp4,  "Here! begins your love story. You take however you wish to take further.", "dev", "Walk towards a beautiful girl standing all alone who seems to be lost.", 5, "end", "bad")

    #Level 5
    sp9 = add_sp(story, 9, sp5,  "Out of the bunch, one seems to be quite attractive, smart, intelligent and sensible. But doesn't seem to show much interst in you.", "dev", "Loving the attention", 5, "end", "bad")
    sp10 = add_sp(story, 10, sp5,  "Sorry, you lost the chance to explore any love. Better try next time!", "dev", "Ooh yuck! they are surely disgusting.", 10,"end", "bad")

    sp11 = add_sp(story, 11, sp9,  "He agrees and here starts your new love story. Let's see where you take this.", "dev", "you invite him for a date.", 5, "end", "bad")
    sp12 = add_sp(story, 12, sp9,  "Bad luck! Another girl comes takes him sneakily and you keep looking.", "dev", "Decide to throw your charm and let him approach you.", 10, "end", "good")


# sid - story_id; n - name; desc - description
def add_story(n, desc, pic):

    path = "./populate_img/stories/"+pic+".jpg"
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

    path = "./populate_img/points/"+pic+".jpg"
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
