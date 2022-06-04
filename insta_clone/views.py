from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    title='welcome'
    
    return render(request,'insta/index.html',{'title':title})

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username, password=password)