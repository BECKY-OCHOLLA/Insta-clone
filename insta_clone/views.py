from django.shortcuts import render,redirect
from .models import Image,Profile, Comment
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic import ListView, DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from dataclasses import fields
from django.urls import reverse






# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    context = {
    'posts':Post.objects.all()
    }
    
    return render(request, 'insta/index.html',context)

# class PostListView(ListView):
#     model=Post
#     template_name='index.html'
#     context_obj='posts'

class DetailView(DetailView):
    model=Post
    template='index.html'
    context_obj='post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'caption', 'image']
    # template_name = 'insta/post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'image', 'caption']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_function(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        else:
            return False

@login_required(login_url='/accounts/login/')
def create_post(request):
    current_user = request.user

    if request.method == 'POST':
        form = UpdateForm(request.POST,request.FILES)
        if form.is_valid():
            p_form = form.save(commit=False)
            p_form.user = current_user

            p_form.save()
        return redirect('home')
    else:
        form = UpdateForm()
    return render(request,'newpost.html',{"form":form})

def likes(request,pk):
    post = Post.objects.get(pk=pk)
    post.likes+=1
    post.save()
    return redirect('home')

def search_results(request):
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"posts": searched_posts})
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f' Account for {username} has been created successfully!')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'django_registration/registration_form.html', {'form':form})

def profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if  prof_form.is_valid():
            user_form.save()
            prof_form.save()

            return redirect('profile')

    else:
        
        prof_form = ProfileUpdateForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        context = {
            'user_form':user_form,
            'prof_form': prof_form
        }

        return render(request, 'profile/profile.html', context)

