from rest_framework import serializers
from .models import Profile, Post, Rating
from awardsapp import forms

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','profile_pic','bio')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields =('id','title', 'description','posted_at','technologies')
