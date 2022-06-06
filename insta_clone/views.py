from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile, Comment
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import ProfileForm,ImageForm,CommentForm


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    image = Image.objects.all()
    return render(request, 'insta/index.html',{'image':image})
