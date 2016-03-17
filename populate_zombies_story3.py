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
    story = add_story("Zombies in Cave", "There is no light but seems like there is fire coming towards you", "dev")

    # # Level 1
    sp1 = add_sp(story, 1, None,  "You are in Boydd Orr, and you have just explored a cave underneath.", "dev", None, 10, "start", None)

    # Level 2
    sp2 = add_sp(story, 2, sp1,  "You are delighted to come as you notice that all your classmates are having a party. ",  "dev", "You dare to go in.",10, "mid", None)
    sp3 = add_sp(story, 3, sp1,  "O no! you missed the party, all your friends were enjoying in that cave. Awesome!!", "dev", "You are scared, so turn the other way.", 10, "end", None)

    # Level 3
    sp4 = add_sp(story, 4, sp2,  "O so you see Zombies have decided to come and dance with you. ", "dev", "Surprise on the dance floor for you.", 10, "mid", "bad")
    sp5 = add_sp(story, 5, sp2,  "O no! you need to rush to the toilet. You got food poisioning.. Aaaaaaaaaaaaah!", "dev", "Have some free food.", 10, "end", None)
    sp6 = add_sp(story, 6, sp2,  "Someone proposed you to have a ball dance with you..", "dev", "Time to socialize", 10, "mid", None)

    #Level 4
    sp7 = add_sp(story, 7, sp4,  "Suddenly one Zombie pushes you in the deepest end of the cave.", "dev", "you are brave and wouldn't mind", 10, "mid", None)
    sp8 = add_sp(story, 8, sp4,  "Aha!! You bump into a lecturer who's really hot!!", "dev", "You decide to sneakily run", 5, "end", "bad")

    #Level 5
    sp9 = add_sp(story, 9, sp6,  "And here the lights are gone and you make the most of your time.", "dev", "You accept", 5, "end", "bad")
    sp10 = add_sp(story, 10, sp6,  "O no! Too late in deciding and you missed a golden opportunity as your best friend has now taken the offer.", "dev", "you decline because you are embarrased.", 10,"end", "bad")

    sp11 = add_sp(story, 11, sp7,  "You end up in a hole, and stuck forever.", "dev", "You see an exit and move towards it.", 5, "end", "bad")
    sp12 = add_sp(story, 12, sp7,  "Congratulations!! you are a millionnaire now as you got a solitaire in the treasure..", "dev", "You see treasure on your left and decide to grab before you go.", 10, "end", "good")


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
