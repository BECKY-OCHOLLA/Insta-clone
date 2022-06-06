from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    Profile_photo = models.ImageField(upload_to = 'images/',blank=True)
    bio=models.TextField(blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)


    @classmethod
    def get_by_id(cls, id):
        details = Profile.objects.get(user = id)
        return details

    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user = id).first()
        return details
    
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


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =30)
    image_caption = models.TextField(max_length =40)
    likes = models.CharField(max_length =20,blank =True)
    profile = models.ForeignKey(Profile, null = True,related_name='image',on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    comment = models.ForeignKey
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
   

class Comment(models.Model):
    comment = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment




   