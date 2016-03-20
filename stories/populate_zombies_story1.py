from story_functions import add_story
from story_functions import add_sp


def populate():
    # the story name has to be unique
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


if __name__ == '__main__':
    print "Starting Zombies population script..."
    populate()
