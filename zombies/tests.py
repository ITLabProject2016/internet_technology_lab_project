from django.test import TestCase
from zombies.models import Story,StoryPoint,UserProfile
from django.core.urlresolvers import reverse
from zombies.views import index
from zombies.views import about
from django.core.urlresolvers import resolve
from django.test import Client



# Test cases for URL

class URLTests(TestCase):

        def test_root_url_resolves_to_index_view(self):
            found = resolve('/zombies/')
            self.assertEqual(found.func, index)


        def test_root_url_resolves_to_about_view(self):
            found = resolve('/zombies/about/')
            self.assertEqual(found.func, about)




# Test cases for Views

class ViewTests(TestCase):

        def test_index_view_test_no_story(self):
           c = Client()
           response = c.get("/zombies/")
           self.assertEquals(response.status_code,200)
           self.assertContains(response,"There are no stories present")
           self.assertContains(response, "Welcome to the campus, stranger. Where will the night take you?.")
 

        def test_index_view_test_one_story(self):

           story = Story(name="Zombies on Campus",visits=1,description='Zombies desciption',picture='testpic')
           story.save()
           c = Client()
           response = c.get("/zombies/")
           self.assertEquals(response.status_code,200)
           self.assertContains(response, "Welcome to the campus, stranger. Where will the night take you?.")
           self.assertContains(response,"/zombies/story-point/1/1/")
           self.assertContains(response,"Zombies on Campus")

           num_stories =len(response.context['stories'])
           self.assertEquals(num_stories,1)


        def test_index_view_test_one_story_no_storyPoint(self):

           story = Story(name="Zombies on Campus",visits=1,description='Zombies desciption',picture='testpic')
           story.save()
           c = Client()
           response = c.get("/zombies/")
           self.assertEquals(response.status_code,200)
           self.assertContains(response,"/zombies/story-point/1/1/")
           num_stories =len(response.context['stories'])
           self.assertEquals(num_stories,1)

           response = c.get("/zombies/story-point/sid=1/spid=1/")
           self.assertEquals(response.status_code,404)


        def test_index_view_test_one_story_one_storyPoint(self):

           story = Story(name="Zombies on Campus",visits=1,description='Zombies desciption',picture='testpic')
           story.save()
           storyPoint = StoryPoint(description='You are in the library',choiceText='yes',experience=10,story_type='start',main_story_id_id=1,visits=1,story_point_id=1,picture='testpic2')
           storyPoint.save()


           c = Client()
           response = c.get("/zombies/")
           self.assertEquals(response.status_code,200)
           self.assertContains(response,"/zombies/story-point/1/1/")
           num_stories =len(response.context['stories'])
           self.assertEquals(num_stories,1)

           response = c.get("/zombies/story-point/1/1/")
           self.assertEquals(response.status_code,200)
           self.assertContains(response, "You are in the library")
           self.assertContains(response, "You have reached the end. Congratulations!")
           self.assertContains(response, "Play the story again")
           self.assertContains(response, "Play another story")


# Test cases for Models

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
