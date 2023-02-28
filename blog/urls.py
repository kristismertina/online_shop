from django.urls import re_path, path
from . import views

urlpatterns = [
    # re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^$', views.PostListView.as_view(), name='post_list'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    # path('<slug:slug>/', views.post_detail, name='post_detail')
    # re_path(r'^$', views.CommentListView.as_view(), name='comment'),

    # path('post/<int:slug>/comments', views.detail, name='comments'),
    
]