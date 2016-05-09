#encoding:utf-8
from django.conf.urls import url
from django.contrib import admin

from comments.api.views import (
    CommentListAPIView,
    CommentDetailAPIView,
    )
#
urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', CommentDetailAPIView.as_view(), name='detail'),

    # url(r'^(?P<id>\d+)/$', comment_thread, name='thread'),
    # url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]
