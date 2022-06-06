from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index,name='index'),
    path("search/", views.search, name="search"),
    path("profile/(<profile>", views.profile, name="profile"),
    path("like/<like>", views.like, name="like"),
    path("like_post/<like_post>", views.like_post, name="like_post"),
    path("post/<post>", views.post, name="post"),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

