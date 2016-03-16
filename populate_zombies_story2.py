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
    story = add_story("Zombies in Space", "Experience and academic zombie space adventure!", "dev")

    # # Level 1
    sp1 = add_sp(story, 1, None,  "You are in University of Glasgow academic space station when alien zombies start to appear from nowhere.", "dev", None, 10, "start", None)

    # Level 2
    sp2 = add_sp(story, 2, sp1,  "You rush into the escape pods but there is one hungy zombie in your way",  "dev", "Go go to the escape pods.",10, "mid", None)
    sp3 = add_sp(story, 3, sp1,  "The study place is full of zombies!", "dev", "Go go to the study place. It looks safe...", 10, "mid", None)
    sp4 = add_sp(story, 4, sp1,  "You close the gates, send the transmit signal and wait there drinking hot chocolate, in five days a rescue group finds and saves you!", "dev", "Go to the transmission station to broadcast a help signal", 10, "end", "good")

    # Level 3
    sp5 = add_sp(story, 5, sp2,  "Zombies have a really cold sense of humor, and you are dead!", "dev", "Tell him a joke!", 10, "end", "bad")
    sp6 = add_sp(story, 6, sp2,  "Ok you can run but so can the Zombie!", "dev", "Try to run!", 10, "mid", None)
    sp7 = add_sp(story, 7, sp2,  "Ok... even though your aim sucks because the only thing you do is spend your life writing code, you managed somehow to cripple it and now it is slower", "dev", "Try to kill it by throwing stuff to it!", 10, "mid", None)

    sp8 = add_sp(story, 8, sp3,  "You did it! shhh...", "dev", "Try to leave as sneaky as you came...", 10, "mid", None)
    sp9 = add_sp(story, 9, sp3,  "The academic zombies get you! Bad Luck!", "dev", "Try to run!", 5, "end", "bad")

    #Level 4
    sp10 = add_sp(story, 10, sp6,  "The Zombie got you!!!", "dev", "Run faster!!!", 5, "end", "bad")
    sp11 = add_sp(story, 11, sp6,  "You are in the escape pod with a preset route to earth! you are saved!", "dev", "Close the Gate!", 10,"end", "bad")

    sp12 = add_sp(story, 12, sp7,  "You got into the escape pod... But the zombie followed you!", "dev", "Try to get in the escape pod", 5, "end", "bad")
    sp13 = add_sp(story, 13, sp7,  "You kill the Zombie and you escape the station with the escape pods!", "dev", "Kill it now that you have the chance", 10, "end", "good")

    sp14 = add_sp(story, 14, sp8,  "You cant find a cure for the zombies because you are a software engineer remeber???", "dev", "On your way around you find the biology lab", 5, "end", "good")
    sp15 = add_sp(story, 15, sp8,  "You struggle to build a killing Robot with RoboJango! Your robot saves you!!!", "dev", "On your way around you find the robot lab", 5, "end", "bad")


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
