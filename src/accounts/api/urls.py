#encoding:utf-8
from django.conf.urls import url

from accounts.api.views import (
    UserCreateAPIView,
    UserLoginAPIView,
    )
#
urlpatterns = [
    # url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    # url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/edit/$', CommentDetailAPIView.as_view(), name='edit'),

    # url(r'^(?P<id>\d+)/$', comment_thread, name='thread'),
    # url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]
