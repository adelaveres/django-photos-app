from django.conf.urls import url
from . import views

app_name = 'photos'

urlpatterns = [
    # /photos/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /photos/4/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]