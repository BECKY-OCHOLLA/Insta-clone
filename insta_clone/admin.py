from django.contrib import admin
from .models import Image,UserProfile,Comment

# Register your models here.


admin.site.register(Image)
admin.site.register(UserProfile)
admin.site.register(Comment)
