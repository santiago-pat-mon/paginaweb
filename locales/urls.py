from django.urls import path
from .views import get_index
from posts.views import home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',get_index, name = 'indexLocales'),
    path('posts',home, name = 'indexPosts')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
