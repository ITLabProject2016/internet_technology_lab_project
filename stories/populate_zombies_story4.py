import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zombies_on_campus.settings')

import django
django.setup()

from story_functions import add_story
from story_functions import add_sp


def populate():
    story = add_story("Love Story in Campus", " Wonderful days were those", "love")

    # Level 1
    sp1 = add_sp(story, 1, None,  "It is your first day in university. You are heart broken, and have just been dumped. However, you came with the hope and desire to explore something new and exciting.",
                 "univ", None, 10, "start", None)

    # Level 2
    sp2 = add_sp(story, 2, sp1,  "You see a bunch of folks: on left there's a gang of hot girls and on your right there's a gang of sexy boys.",
                 "left-right", "Go to the cafe",10, "mid", None)
    sp3 = add_sp(story, 3, sp1,  "You ask at the desk for your student ID, but suddenly you hear someone shouting your name.",
                 "shout", "Go to the registration office", 10, "mid", None)

    # Level 3
    sp4 = add_sp(story, 4, sp2, "Nah! The girls were not interesting, they did not entertain you.",
                 "left-right", "Go to the left", 10, "mid", "bad")
    sp5 = add_sp(story, 5, sp2, "Ooh la la! All the boys are drooling at you!",
                 "zombie_3", "Go to the right", 10, "mid", None)

    sp6 = add_sp(story, 6, sp3, "Oh dear! Be adventurous, and at least a little vigilant. You can't keep missing opportunities like these!",
                 "no-love", "You ignore", 10, "end", None)
    sp7 = add_sp(story, 7, sp3,  "Such a dreamer you are. It's fire alarm, you better run, or else you might get burnt!",
                 "no-love", "You turn with a smile thinking you found your new love", 10, "end", None)

    #Level 4
    sp8 = add_sp(story, 8, sp4, "Love-luck is not in your favour. You better concentrate on your studies, so at least you can stabilise your career!",
                 "no-love", "Simply disheartened, and go to your lectures", 10, "end", None)
    sp9 = add_sp(story, 9, sp4, "Here begins your love story! You take it however you wish to take further.",
                 "couple-love2", "Walk towards a beautiful girl standing all alone who seems to be lost", 5, "end", "good")


    sp10 = add_sp(story, 10, sp5, "Out of the bunch, one seems to be quite attractive, smart, intelligent and sensible. But doesn't seem to show much interest in you.",
                  "zombie_3", "Loving the attention", 5, "mid", None)
    sp11 = add_sp(story, 11, sp5, "Sorry, you lost the chance to explore love! Better luck next time!", "no-love",
                  "Ooh, yuck! They are surely disgusting", 10,"end", "bad")

    #Level 5
    sp12 = add_sp(story, 12, sp10, "He agrees and here starts your new love story. Let's see where you take this.",
                  "couple-love", "You invite him for a date", 5, "end", "good")
    sp13 = add_sp(story, 13, sp10, "Bad luck! Another girl comes takes him sneakily and you are left looking for another boy.", "no-love",
                  "Decide to throw your charm and let him approach you", 10, "end", "bad")


if __name__ == '__main__':
    print "Starting Zombies population script..."
    populate()
