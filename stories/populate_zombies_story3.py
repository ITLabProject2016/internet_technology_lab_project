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
from story_functions import add_story
from story_functions import add_sp


def populate():
    # the story name has to be unique
    story = add_story("Zombies in Cave", "There is no light but seems like there is fire coming towards you", "cave")

    # # Level 1
    sp1 = add_sp(story, 1, None, "You are in Boydd Orr, and you have just explored a cave underneath.", "bo_floor",
                 None, 10, "start", None)

    # Level 2
    sp2 = add_sp(story, 2, sp1, "You are delighted to come as you notice that all your classmates are having a party. ",
                 "party1", "You dare to go in.", 10, "mid", None)
    sp3 = add_sp(story, 3, sp1, "O no! you missed the party, all your friends were enjoying in that cave. Awesome!!",
                 "no_love_study", "You are scared, so turn the other way.", 10, "end", None)

    # Level 3
    sp4 = add_sp(story, 4, sp2, "O so you see Zombies have decided to come and dance with you. ", "zombie_2",
                 "Surprise on the dance floor for you.", 10, "mid", "bad")
    sp5 = add_sp(story, 5, sp2, "O no! you need to rush to the toilet. You got food poisioning.. Aaaaaaaaaaaaah!",
                 "zombie_5", "Have some free food.", 10, "end", None)
    sp6 = add_sp(story, 6, sp2, "Someone proposed you to have a ball dance with you..", "zombie_1", "Time to socialize",
                 10, "mid", None)

    # Level 4
    sp7 = add_sp(story, 7, sp4, "Suddenly one Zombie pushes you in the deepest end of the cave.", "corridor_1",
                 "you are brave and wouldn't mind", 10, "mid", None)
    sp8 = add_sp(story, 8, sp4, "Aha!! You bump into a lecturer who's really hot!!", "couple-love2",
                 "You decide to sneakily run", 5, "end", "bad")

    # Level 5
    sp9 = add_sp(story, 9, sp6, "And here the lights are gone and you make the most of your time.", "couple-love2",
                 "You accept", 5, "end", "bad")
    sp10 = add_sp(story, 10, sp6,
                  "O no! Too late in deciding and you missed a golden opportunity as your best friend has now taken the offer.",
                  "no-love", "you decline because you are embarrased.", 10, "end", "bad")

    sp11 = add_sp(story, 11, sp7, "You end up in a hole, and stuck forever.", "zombie_6",
                  "You see an exit and move towards it.", 5, "end", "bad")
    sp12 = add_sp(story, 12, sp7,
                  "Congratulations!! you are a millionnaire now as you got a solitaire in the treasure..", "party1",
                  "You see treasure on your left and decide to grab before you go.", 10, "end", "good")


if __name__ == '__main__':
    print "Starting Zombies population script..."
    populate()
