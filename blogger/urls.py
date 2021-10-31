from django.conf.urls import url, include
from django.contrib import admin
from .views import HomeView, MusicView, VideoView
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^music/', MusicView.as_view(), name='music'),
    url(r'^video/', VideoView.as_view(), name='video'),
    url(r'^kontak/', include('kontak.urls', namespace='kontak')),
    url(r'^admin/', admin.site.urls),
]
