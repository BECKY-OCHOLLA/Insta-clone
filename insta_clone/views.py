from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    title='welcome'
    
    return render(request,'insta/index.html',{'title':title})
    
@login_required(login_url='/accounts/login/')
def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            if user is not None:
              login(request, user)
              return HttpResponseRedirect(reverse("index"))
             
            else:
                return HttpResponseRedirect(reverse("user_login")) #raise error/ flash
    else:
        return render(request, "auth/login.html", context={})

        ...
  