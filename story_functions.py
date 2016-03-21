import os
import django
from zombies.models import Story, StoryPoint

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zombies_on_campus.settings')
django.setup()


# sid - story_id; n - name; desc - description
def add_story(n, desc, pic):
    path = "img/stories/" + pic + ".jpg"
    story = Story.objects.create(name=n, description=desc, picture=path)
    story.save()
    return story


# Storypoint - story point which is the foreign key (which leads to this sp)
# s_id - story_id
# description - what the user will be shown AFTER selecting this story point
# choice - what the user will be shown BEFORE selecting this story point
# exp - how much experience points the user will get
# type - type of the story point (mid/end/start)
def add_sp(mid, sid, storypoint_parent, desc, pic, choice, exp, typ, end):
    path = "img/points/" + pic + ".jpg"
    sp = StoryPoint.objects.create(
        main_story_id=mid,
        story_point_id=sid,
        parentSP=storypoint_parent,
        description=desc,
        picture=path,
        choiceText=choice,
        experience=exp,
        story_type=typ,
        ending_type=end,
    )
    sp.save()
    return sp
