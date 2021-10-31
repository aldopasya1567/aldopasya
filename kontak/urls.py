from django.conf.urls import url
from .views import KontakView, HomeView, DetailViews, FormViews, DeleteViews, UpdateViews
from .models import Post

urlpatterns = [
    url(r'^delete/(?P<pk>\d+)$', DeleteViews.as_view(), name='delete'),
    url(r'^update/(?P<pk>\d+)$', UpdateViews.as_view(), name='update'),
    url(r'^$', KontakView.as_view(), name='list'),
    url(r'^home/', HomeView.as_view(), name='home'),
    url(r'^detail/(?P<slug>[\w-]+)$', DetailViews.as_view(), name='detail'),
    url(r'^create/$', FormViews.as_view(), name='create')
]