from .models import Profile, Post, Rating
from django import forms


class UploadPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile']
        
class DetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['score','user','post']