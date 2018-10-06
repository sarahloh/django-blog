from django.urls import path, re_path
from .views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    path('', get_posts, name='get_posts'),
    re_path('^(?P(<pk>\d+)/$', post_detail, name='post_detail'),
    path('new/', create_or_edit_post, name='new_post'),
    re_path('^(?P(<pk>\d+)/edit/$', post_detail, name='edit_post'),
]
