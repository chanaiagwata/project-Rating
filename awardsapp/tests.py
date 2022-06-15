from django.test import TestCase
from .models import Post, Profile, Rating, User


# Create your tests here.




class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='chanai')
        self.profile = Profile.objects.create(user = self.user,bio = 'simba')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

  
class PostTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='chanai')
        self.profile = Profile.objects.create(user = self.user,bio = 'layoni')

        self.project = Post.objects.create(user = self.user,profile = self.profile,title = 'Awardss',location='Nairobi',description='Avengers Assemble',link= 'chanai-gallery.herokuapp.com/',date='06/06/2022', technologies='Django')

    def test_instance(self):
        self.assertTrue(isinstance(self.project,Post))
    
    
    def test_save_project(self):
        self.project.save_post()
        project = Post.objects.all()
        self.assertTrue(len(project) > 0)
    
    def test_delete_project(self):
        self.project.delete_post()
        project = Post.search_by_posts('Awardss')
        self.assertTrue(len(project) < 1)


    def test_find_project(self):
        self.project.save()
        project = Post.search_by_posts('Awardss')
        self.assertTrue(len(project) > 0)
        

 