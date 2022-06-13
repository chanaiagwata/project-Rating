from pyexpat import model
from .models import Profile, Post, Rating
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile','posted_at']
        
class DetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
class PostForm(forms.ModelForm):
    project_pic= forms.ImageField(label='')
    
    class Meta:
        model = Post
        exclude = ['user','posted_at']
        
class RatingsFrom(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['score','user','post']