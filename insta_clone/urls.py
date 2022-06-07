from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name='index'),
    path('<int:pk>',views.likes, name='likes'),
    path('create_post/',views.create_post,name='create_post'),
    path('search/',views.search_results,name='search_results'),
    path('logout/',views.logout, name='logout'),
    path('profile/',views.profile, name='profile'),
  
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

