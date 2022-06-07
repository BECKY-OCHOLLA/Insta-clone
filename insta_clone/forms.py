from django import forms
from .models import Image, Profile, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['Likes', 'pub_date', 'Profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']
