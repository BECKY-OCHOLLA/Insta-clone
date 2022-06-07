from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UpdateForm(forms.ModelForm):
    """
    class that handles forms
    """

    class Meta:
        model=Post

        fields=['image','title','caption']
        exclude=['likes','pub_date','comments','user']

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment...'


    class Meta:
        model= Comment
        fields=['comment']

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    bio = forms.CharField() 

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['image']