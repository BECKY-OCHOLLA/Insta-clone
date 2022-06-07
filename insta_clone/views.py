from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile, Comment
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import ProfileForm,ImageForm,CommentForm


# Create your views here.

# @login_required(login_url='/accounts/login/')
def index(request):
    image = Image.objects.all()
    return render(request, 'insta/index.html',{'image':image})


def search(request):

    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("profile")
        profile = Profile.search_user(search_term)
        message = f"{search_term}"
       
        return render(request,'insta/search_results.html',{'message':message, 'profile':profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'insta/search_results.html',{'message':message})


# @login_required
def profile(request, username):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id=user)
    posts = Image.objects.filter(profile__id=id)[::-1]
    return render(request, "insta/profile.html", {"user":user,"profile":profile,"posts":posts})




def logout(request):
    return render(request, 'insta/index.html')

def view_image(request):
    image = Image.objects.all()
    return render(request, 'insta/index.html',{"image":image})


# @login_required(login_url='/accounts/login')
def upload_image(request):
    if request.method == 'POST':
        uploadform = ImageForm(request.POST, request.FILES)
        if uploadform.is_valid():
            upload = uploadform.save(commit=False)
            upload.profile = request.user.profile
            upload.save()
            return redirect('profile', username=request.user)
    else:
        uploadform = ImageForm()
    
    return render(request, 'insta/profile.html', {'uploadform':uploadform})



def post(request, id):
    post = Image.objects.get(id = id)
    comments = Comment.objects.filter(post__id=id)
    current_user = request.user
    current_profile = Profile.objects.get(post=id)

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


