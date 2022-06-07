from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index,name='index'),
    path("search/", views.search, name="search"),
    path("profile/", views.profile, name="profile"),
    path('upload/', views.upload_image, name='upload_image'),
    # path("like_post/<like_post>", views.like_post, name="like_post"),
    path("post/<post>", views.post, name="post"),
    # path('logout/', views.user_logout, name='user_logout'),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

