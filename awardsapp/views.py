from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Rating
from django.contrib.auth.models import User
from .forms import DetailsForm, UploadPostForm, RatingsForm


# Create your views here.
def index(request):
    posts = Post.objects.all()
    current_user = request.user
    
    if request.method=="POST":
        form = UploadPostForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            post = form.save(commit=False)
            form.save()
        return redirect('indexpage')
    else:
        form=UploadPostForm()
        
    return render(request, 'index.html',{'form':form,'posts':posts})

def profile(request):
    posts = Post.objects.all()
    current_user = request.user 
    
    if request.method=='POST':
        details_form = DetailsForm(request.POST, request.FILES)
        posts_form = UploadPostForm(request.POST, request.FILES)
        
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
        posts_form = UploadPostForm
        
    return render(request,'profile.html', {'details_form':details_form, 'posts_form':posts_form, 'posts':posts,})

def update_profile(request):
    current_user = request.user
    if request.method== 'POST':
        form = DetailsForm(request.POST, request.FILES)
        if form.is_valid():
            Profile.objects.filter(id=current_user.profile.id).update(bio=form.cleaned_data["bio"])
            profile = Profile.objects.filter(id=current_user.profile.id).first()
            profile.profile_pic.delete()
            profile.profile_pic=form.cleaned_data["profile_pic"]
            profile.save()
        return redirect('profile')
    else:
        form = DetailsForm()
    return render(request, 'update_profile.html', {"form":form})

def project(request, post):
    post = Post.objects.get(title=post)
    rating = Rating.objects.filter(user=request.user, post=post).first()
      
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.post = post
            rate.save()
            
            post_ratings = Rating.objects.filter(post=post)
            
            
            design_ratings = [designrates.design for designrates in post_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [usabilityrates.usability for usabilityrates in post_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [contentrates.content for contentrates in post_ratings]
            content_average = sum(content_ratings) / len(content_ratings)
            
            total_average_score = (design_average+usability_average+content_average)/3
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.total_average_score = round(total_average_score, 2)
            rate.save()
            
            return HttpResponseRedirect(request.path_info)
        else:
            form = RatingsForm()
        elements = {
            'post':post,
            'rating_form':form,
        }
        return render(request, 'project.html', elements)
            