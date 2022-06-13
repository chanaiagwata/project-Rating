from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=120)
    profile_pic = models.ImageField(upload_to = 'images/')
    bio = models.TextField(max_length=240, null=True)
    
    def __str__(self):
        return self.user

class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    pic = models.ImageField(upload_to = 'posts/', blank=False)
    description = models.TextField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return {self.title}
    
class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=rating, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return {self.user}