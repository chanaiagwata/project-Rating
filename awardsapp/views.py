from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Rating
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

