from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=144, blank=True, default="Post")
    caption = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class UserProfile(models.Model):
    # User=models.ForeignKey(User, on_delete=models.CASCADE)
    profile_Photo=CloudinaryField('image')
    bio=models.TextField(blank=True)
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)

    def __str__(self):
        return self.bio

    @classmethod
    def search_user(cls,search_term):
        theuser = cls.objects.filter(user__icontains=search_term)
        return theuser


    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_caption(self, new_cap):
        self.caption = new_cap
        self.save()    

class Comment(models.Model):
    comment = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment




   