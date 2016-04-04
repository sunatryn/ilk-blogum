from django.conf.urls import url
from . import views

urlpatterns = [
# Django'ya eğer siteye biri 'http://127.0.0.1:8000/' adresinden gelirse
# gitmesi gereken yerin views.post_list olduğunu söylüyor.
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
