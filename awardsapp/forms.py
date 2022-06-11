from .models import Profile, Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile']
        
class DetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']