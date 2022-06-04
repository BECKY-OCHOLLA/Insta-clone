from django.shortcuts import render

# Create your views here.

def index(request):
    title='welcome'
    return render(request,'insta/index.html',{'title':title})