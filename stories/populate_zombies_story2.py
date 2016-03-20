import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zombies_on_campus.settings')

import django
django.setup()

from story_functions import add_story
from story_functions import add_sp


def populate():
    story = add_story("Zombies in Space", "Experience and academic zombie space adventure!", "space_station")

    # Level 1
    sp1 = add_sp(story, 1, None,  "You are in University of Glasgow academic space station when alien zombies start to appear from nowhere.", "space_station", None, 10, "start", None)

    # Level 2
    sp2 = add_sp(story, 2, sp1,  "You rush into the escape pods but there is one hungry zombie in your way",  "zombie_1", "Go go to the escape pods.",10, "mid", None)
    sp3 = add_sp(story, 3, sp1,  "The study place is full of zombies!", "space_study", "Go go to the study place. It looks safe...", 10, "mid", None)
    sp4 = add_sp(story, 4, sp1,  "You close the gates, send the transmit signal and wait there drinking hot chocolate. In five days a rescue group finds and saves you!", "space_command_station",
                 "Go to the transmission station to broadcast a help signal", 10, "end", "good")

    # Level 3
    sp5 = add_sp(story, 5, sp2,  "Zombies have a really cold sense of humor...", "zombie_3", "Tell him a joke!", 10, "end", "bad")
    sp6 = add_sp(story, 6, sp2,  "You can run, but so can the Zombie!", "zombie_4", "Try to run!", 10, "mid", None)
    sp7 = add_sp(story, 7, sp2,  "Even though your aim sucks (the only thing you do is spend your life writing code), you manage to somehow cripple it and now it is slower.",
                 "zombie_5", "Try to kill it by throwing stuff at it!", 10, "mid", None)

    sp8 = add_sp(story, 8, sp3,  "You did it! Shhh... You are out of the study place in the hallway...", "space_hallway", "Try to leave as sneaky as you came...", 10, "mid", None)
    sp9 = add_sp(story, 9, sp3,  "The academic zombies get you! Bad Luck!", "sci_zombie", "Try to run!", 5, "end", "bad")

    #Level 4
    sp10 = add_sp(story, 10, sp6,  "The Zombie got you!", "zombie_4", "Run faster!!!", 5, "end", "bad")
    sp11 = add_sp(story, 11, sp6,  "You are in the escape pod with a preset route back to Earth! you are saved!", "escape_pods", "Close the Gate!", 10,"end", "bad")

    sp12 = add_sp(story, 12, sp7,  "You got into the escape pod... But the zombie followed you!", "zombie_5", "Try to get in the escape pod", 5, "end", "bad")
    sp13 = add_sp(story, 13, sp7,  "You kill the Zombie and you escape the station with the escape pods!", "pod_drop", "Kill it now that you have the chance", 10, "end", "good")

    sp14 = add_sp(story, 14, sp8,  "You cant find a cure for the zombies because you are a software engineer, remember?!", "lab", "On your way around you find the biology lab", 5, "end", "good")
    sp15 = add_sp(story, 15, sp8,  "You struggle to build a killing Robot with RoboJango! Your robot saves you!", "robot_lab", "On your way around you find the robot lab", 5, "end", "bad")


if __name__ == '__main__':
    print "Starting Zombies population script..."
    populate()
