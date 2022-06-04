from django.shortcuts import render
# from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    title='welcome'
    
    return render(request,'insta/index.html',{'title':title})

# @login_required(login_url='/accounts/login/')
# def article(request, article_id):
    