from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image, User, Profile, Comment
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
# from .forms import CommentForm,UserForm


# Create your views here.

@login_required
def index(request):
    title = 'Instagram'
    current_user = request.user
    profile = Profile.get_profile()
    image = Image.get_images()
    comments = Comment.get_comment()
    return render(request,'insta/index.html',{"title":title,
                                        "profile":profile,
                                        "comments":comments,
                                        "current_user":current_user,
                                        "images":image,})

def search(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_user = UserProfile.search_user(search_term)
        message = f"{search_term}"
        user = User.objects.all()
        context = {
            "user":user,
            "message":message,
            "profile":searched_user
        }
        return render(request,'insta/search_results.html',context)

    else:
        message = "You haven't searched for any term"
        return render(request, 'insta/search_results.html',{"message":message})


@login_required
def profile(request, id):
    user = User.objects.get(id=id)
    profile = UserProfile.objects.get(user_id=user)
    posts = Image.objects.filter(profile__id=id)[::-1]
    return render(request, "insta/profile.html", context={"user":user,"profile":profile,"posts":posts})


@login_required
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
        return render(request, "registration/login.html", context={})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user_login"))

def post(request, id):
    post = Image.objects.get(id = id)
    comments = Comment.objects.filter(post__id=id)
    current_user = request.user
    current_profile = UserProfile.objects.get(post=id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = current_user
            comment.post = post
            comment.save()
            comment_form = CommentForm()
            return redirect("post", post.id)

    else:
        comment_form = CommentForm()

    return render(request, "insta/post.html", context={"post":post,"current_user":current_user,"current_profile":current_profile,"comment_form":comment_form,
                                                          "comments":comments,})


def like(request, id):
    post = Image.objects.get(id = id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse("index"))


def like_post(request, id):
    post = Image.objects.get(id = id)
    post.likes += 1
    post.save()
    return redirect("post", post.id)

def register(request):
    registered = False
    

    if request.method == "POST":
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = UserProfile()
            user_profile.user = user
            # user_profile.save()
            user_profile.save()
            registered = True
            

            return HttpResponseRedirect(reverse("user_login"))

        else:
            pass

    else:
        user_form = UserForm()
        

    return render(request, "registration/register.html", context={"user_form":user_form,
                                                          "registered":registered})



  