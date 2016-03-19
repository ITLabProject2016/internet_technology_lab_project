from django.test import TestCase
from zombies.models import Story,StoryPoint,UserProfile


class StoryMethodTests(TestCase):

    def test_ensure_story_is_inserted(self):

        story = Story(name="Zombies on Campus",visits=1,description='Zombies desciption',picture='testpic')
        story.save()
        self.assertEquals((story.visits==1), True)
        self.assertEquals((story.name=='Zombies on Campus'), True)
        self.assertEquals((story.description=='Zombies desciption'), True)
        self.assertEquals((story.picture=='testpic'), True)



    def test_ensure_storyPoints_is_inserted(self):

        storyPoint = StoryPoint(description='You are in the library',choiceText='yes',experience=10,story_type='start',main_story_id_id=5,visits=1,story_point_id=1,picture='testpic2')
        storyPoint.save()
        self.assertEquals((storyPoint.description=='You are in the library'),True)
        self.assertEquals((storyPoint.choiceText=='yes'),True)
        self.assertEquals((storyPoint.experience==10),True)
        self.assertEquals((storyPoint.story_type=="start"),True)
        self.assertEquals((storyPoint.story_point_id==1),True)
        self.assertEquals((storyPoint.picture=='testpic2'),True)
        self.assertEquals((storyPoint.visits==1),True)
        self.assertEquals((storyPoint.main_story_id_id==5),True)



    def test_ensure_userProfile_is_inserted(self):

        userProfile = UserProfile(user_id=123,exp=1,finished_stories=3,picture='testpic3')
        userProfile.save()
        self.assertEquals((userProfile.user_id==123), True)
        self.assertEquals((userProfile.exp==1), True)
        self.assertEquals((userProfile.finished_stories==3), True)
        self.assertEquals((userProfile.picture=='testpic3'), True)