from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from models import Story


class StoryMethodTests(TestCase):

    def test_ensure_story_is_inserted(self):

        story = Story(name="Zombies on Campus",visits=1,description='Zombies desciption',picture='testpic')
        story.save()
        self.assertEquals((story.visits==1), True)
        self.assertEquals((story.name=='Zombies on Campus'), True)
        self.assertEquals((story.description=='Zombies desciption'), True)
        self.assertEquals((story.picture=='testpic'), True)