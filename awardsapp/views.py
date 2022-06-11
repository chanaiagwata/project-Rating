from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Rating
from django.contrib.auth.models import User
from .forms import DetailsForm, PostForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    posts = Post.objects.all()
    current_user = request.user 
    
    if request.method=='POST':
        details_form = DetailsForm(request.POST, request.FILES)
        posts_form = PostForm(request.POST, request.FILES)
        
        if details_form.is_valid():
            profile = details_form.save(commit=False)
            profile.user = current_user
            profile.save()
            
        if posts_form.is_valid():
            post = posts_form.save(commit=False)
            post.profile = current_user.profile
            posts_form.save()
            
        return redirect('profile')
        
    else:
        details_form = DetailsForm
        posts_form = PostForm
        
    return render(request,'profile.html', {'details_form':details_form, 'posts_form':posts_form, 'posts':posts,})
