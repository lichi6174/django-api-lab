#encoding:utf-8
from django.conf.urls import url
from django.contrib import admin

from comments.api.views import (
    CommentCreateAPIView,
    CommentListAPIView,
    CommentDetailAPIView,
    )
#
urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='detail'),

    # url(r'^(?P<id>\d+)/$', comment_thread, name='thread'),
    # url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]
