from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.main, name = "main"),
    url(r'^blog/(?P<blog_id>[0-9]+)$', views.display, name = "display"),
]
