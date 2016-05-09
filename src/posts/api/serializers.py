from rest_framework.serializers import ModelSerializer

from posts.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'title',
            # 'slug',
            'content',
            'publish',
        ]

class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'slug',
            'content',
            'publish',
        ]

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'content',
            'publish',
        ]


"""

from posts.models import Post
from posts.api.serializers import PostDetailSerializer


data = {
    "title": "Yeah buddy",
    "content": "New content",
    "publish": "2016-5-5",
    "slug": "yeah-buddy",
}

obj = Post.objects.get(id=1)
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)
"""