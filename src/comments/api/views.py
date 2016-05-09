#encoding:utf-8
from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)

from posts.api.permissions import IsOwerOrReadOnly
from posts.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination

from comments.models import Comment

from comments.api.serializers import (
    CommentSerializer,
)

# class PostCreateAPIView(CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostCreateUpdateSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user,title="My title")
#         serializer.save(user=self.request.user)


class CommentListAPIView(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content','user__first_name']  #http://127.0.0.1:8000/api/posts/?search=post&q=better&ordering=-title
    # pagination_class = LimitOffsetPagination #PageNumberPagination
    # pagination_class = PostLimitOffsetPagination #PageNumberPagination
    pagination_class = PostPageNumberPagination #PageNumberPagination


    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(PostListAPIView,self).get_queryset(*args, **kwargs)
        queryset_list = Comment.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(content__icontains=query)|
                    Q(user__first_name__icontains=query)|
                    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # lookup_field = 'slug'

# class PostUpdateAPIView(RetrieveUpdateAPIView):
# # class PostUpdateAPIView(UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostCreateUpdateSerializer
#     # serializer_class = UpdateAPIView
#     lookup_field = 'slug'
#     permission_classes = [IsAuthenticatedOrReadOnly,IsOwerOrReadOnly]
#
#     def perform_update(self, serializer):
#         # serializer.save(user=self.request.user,title="My title")
#         serializer.save(user=self.request.user)

# class PostDeleteAPIView(DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostDetailSerializer
#     lookup_field = 'slug'
#     permission_classes = [IsAuthenticatedOrReadOnly,IsOwerOrReadOnly]

