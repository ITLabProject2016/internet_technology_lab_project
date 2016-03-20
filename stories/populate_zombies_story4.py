import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zombies_on_campus.settings')

import django
django.setup()

from story_functions import add_story
from story_functions import add_sp


def populate():
    story = add_story("Love Story in Campus", " Wonderful days were those", "love")

    # Level 1
    sp1 = add_sp(story, 1, None,  "It is your first day in university. You are heart broken, and have just been_dumped. However, you came with the hope and desire to explore something new and exciting.",
                 "univ", None, 10, "start", None)

    # Level 2
    sp2 = add_sp(story, 2, sp1,  "You see a bunch of folks: on left there's a gang of hot girls and on your right there's a gang of sexy boys.",
                 "left-right", "Go to the cafe",10, "mid", None)
    sp3 = add_sp(story, 3, sp1,  "You ask at the desk for your student ID, but suddenly you hear someone shouting your name.",
                 "shout", "Go to the registration office", 10, "mid", None)

    # Level 3
    sp4 = add_sp(story, 4, sp2, "ooh! the moment you reach closer, you notice they are actually Zombies! EEeeeeeeeeeeeeeek!Let's run out of the cafe..",
                 "left-right", "Go to the left", 10, "mid", "bad")
    sp5 = add_sp(story, 5, sp2, "Ooh la la! All the boys are drooling at you!",
                 "zombie_3", "Go to the right", 10, "mid", None)

    sp6 = add_sp(story, 6, sp3, "Oh dear! Be adventurous, and at least a little vigilant. You can't keep missing opportunities like these!",
                 "no-love", "You ignore", 10, "end", None)
    sp7 = add_sp(story, 7, sp3,  "Such a dreamer you are. It's fire alarm, you better run, or else you might get burnt!",
                 "no-love", "You turn with a smile thinking you found your new love", 10, "end", None)

    #Level 4
    sp8 = add_sp(story, 8, sp4, "Love-luck is not in your favour. You better concentrate on your studies, so at least you can stabilise your career!",
                 "no-love", "You are disheartened, and you go to your lectures", 10, "end", None)
    sp9 = add_sp(story, 9, sp4, "Not bad! so you again took a challenge.. This time you are actually lucky, it's not a zombie this time. You managed to impress a girl and here begins your love story! Now, you take it however you wish to take further.",
                 "couple-love2", "Walk towards a beautiful girl standing all alone who seems to be lost", 5, "end", "good")


    sp10 = add_sp(story, 10, sp5, "Out of the bunch, one seems to be quite attractive, smart, intelligent and sensible. And he proposes you and you accept the offer because it was too good to miss. You sneak away and decide to go in Kelvingrove Park, sitting under a tree, with a romance just beginning and guess what here comes the Zombies from the tree above you.. ",
                  "zombie_3", "Loving the attention", 5, "mid", None)
    sp11 = add_sp(story, 11, sp5, "Woooo! Well done, you managed to save yourself. You are actually lucky because they were real Zombies and that's why they seemed to be desparate... ", "no-love",
                  "Ooh, yuck! They are surely disgusting", 10,"end", "bad")

    #Level 5
    sp12 = add_sp(story, 12, sp10, "O dear! Its not a good idea to be brave all the time as you and your new found love have just been eaten by Zombies. Better take some spontaneous actions sometime. ",
                  "couple-love", "You are brave and just stay there.", 5, "end", "bad")
    sp13 = add_sp(story, 13, sp10, "Bad luck! Such a fool you are, it was just an illusion. Now you just lost your new love. Next time you better think before taking such a quick action.", "no-love",
                  "You scream, leave everything(even your new found love) and run.", 10, "end", "bad")


if __name__ == '__main__':
    print "Starting Zombies population script..."
    populate()
