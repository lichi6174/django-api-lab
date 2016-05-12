#encoding:utf-8
from django.db.models import Q
from django.contrib.auth import get_user_model
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


from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

User = get_user_model()
from accounts.api.serializers import (
    UserCreateSerializer,
)

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()




