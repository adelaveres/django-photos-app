from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'photos'

urlpatterns = [
    # /photos/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /photos/4/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /photos/first_photos/
    url(r'^first_photos/$', views.first_photos, name='first_photos')
]