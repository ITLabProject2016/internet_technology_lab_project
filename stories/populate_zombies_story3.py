import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zombies_on_campus.settings')


import django
django.setup()

from story_functions import add_story
from story_functions import add_sp


def populate():
    story = add_story("Zombies in Cave", "There is no light but it seems like there is fire coming towards you.", "dev")

    # Level 1
    sp1 = add_sp(story, 1, None, "You are in Boyd Orr, and you have just explored a cave underneath it.", "dev", None, 10, "start", None)

    # Level 2
    sp2 = add_sp(story, 2, sp1, "You are delighted to come, as you notice that all your classmates are having a party!",  "dev", "You dare to go in",10, "mid", None)
    sp3 = add_sp(story, 3, sp1, "Oh no! You missed the party that all of your friends were enjoying in the cave. Sad!", "dev", "You are scared, so turn the other way", 10, "end", None)

    # Level 3
    sp4 = add_sp(story, 4, sp2, "You notice that zombies have decided to come and dance with you.", "dev", "Surprise on the dance floor for you", 10, "mid", "bad")
    sp5 = add_sp(story, 5, sp2, "O no! you need to rush to the toilet. You got food poisoning.. Aaaaaaaaaaaaah!", "dev", "Have some free food", 10, "end", None)
    sp6 = add_sp(story, 6, sp2, "Someone asked to have a ball dance with you...", "dev", "Time to socialize", 10, "mid", None)

    #Level 4
    sp7 = add_sp(story, 7, sp4, "Suddenly one zombie pushes you in the deepest end of the cave.", "dev", "You are brave and do not mind", 10, "mid", None)
    sp8 = add_sp(story, 8, sp4, "Aha! You bump into a lecturer who's really hot!!", "dev", "You decide to sneakily run", 5, "end", "bad")

    #Level 5
    sp9 = add_sp(story, 9, sp6, "And here the lights are gone and you make the most of your time.", "dev", "You accept", 5, "end", "bad")
    sp10 = add_sp(story, 10, sp6, "Oh no! You were too slow in making a decision and you missed a golden opportunity, as your best friend has now taken the offer.", "dev",
                  "You decline because you are embarrassed", 10,"end", "bad")

    sp11 = add_sp(story, 11, sp7,  "You end up in a hole, stuck forever.", "dev", "You see an exit and move towards it", 5, "end", "bad")
    sp12 = add_sp(story, 12, sp7,  "Congratulations! You are a millionaire now as you got a solitaire in the treasure!", "dev",
                  "You see treasure on your left and decide to grab before you go!", 10, "end", "good")


if __name__ == '__main__':
    print "Starting Zombies population script..."
    populate()
