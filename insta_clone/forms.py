from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

# class UpdateForm(forms.ModelForm):
#     """
#     class that handles forms
#     """

#     class Meta:
#         model=Post

#         fields=['image','title','caption']
#         exclude=['likes','pub_date','comments','user']

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment...'


    class Meta:
        model= Comment
        fields=['comment']

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email=forms.EmailField()
    email2=forms.EmailField()
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')


    def clean(self, *args, **kwargs):
      
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    bio = forms.CharField() 
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = User
        fields = ['username','email']



class UpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    image_name = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    likes= forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    title= forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = ['image','image_name','caption','likes','title']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['image']