from django.db import models
from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    image=CloudinaryField('images')
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
    def search_by_title(cls,search_term):
        profiles=cls.objects.filter(title__icontains=search_term)
        return profiles

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_caption(self, new_cap):
        self.caption = new_cap
        self.save() 


# Create your models here.
class Post(models.Model):
    image = CloudinaryField('images')
    image_name = models.CharField(max_length =30)
    caption = models.TextField(max_length =40,null=True)
    likes = models.CharField(max_length =20,blank =True)
    title = models.CharField(max_length=100, default='')
    profile = models.ForeignKey(Profile, null = True,related_name='poster',on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    user= models.ForeignKey(Profile, on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    @classmethod
    def get_post(cls):
        post=Post.objects.all()
        return post



    def __str__(self):
        return str(self.caption)

    @classmethod
    def display_posts(cls):
        posts = cls.objects.all().order_by('-posted_at')
        return posts

    def __str__(self):
        return "%s post" % self.image_name    
   

class Comment(models.Model):
    name = models.CharField(max_length=256)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment




   