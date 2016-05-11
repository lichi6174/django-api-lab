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

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

from comments.api.serializers import (
    CommentSerializer,
    CommentListSerializer,
    CommentDetailSerializer,
    create_comment_serializer,
)

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    # serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        model_type = self.request.GET.get('type')
        slug = self.request.GET.get("slug")
        parent_id = self.request.GET.get("parent_id", None)
        return create_comment_serializer(
                model_type=model_type,
                slug=slug,
                parent_id=parent_id,
                user=self.request.user,
        )

    # def perform_create(self, serializer):
    #     # serializer.save(user=self.request.user,title="My title")
    #     serializer.save(user=self.request.user)


class CommentListAPIView(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = CommentListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content','user__first_name']  #http://127.0.0.1:8000/api/posts/?search=post&q=better&ordering=-title
    # pagination_class = LimitOffsetPagination #PageNumberPagination
    # pagination_class = PostLimitOffsetPagination #PageNumberPagination
    pagination_class = PostPageNumberPagination #PageNumberPagination


    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(PostListAPIView,self).get_queryset(*args, **kwargs)
        queryset_list = Comment.objects.filter(id__gte=0)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(content__icontains=query)|
                    Q(user__first_name__icontains=query)|
                    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list


# class CommentEditAPIView(RetrieveAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentDetailSerializer
#     # lookup_field = 'slug'


class CommentDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    queryset = Comment.objects.filter(id__gte=0)
    serializer_class = CommentDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwerOrReadOnly]


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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


