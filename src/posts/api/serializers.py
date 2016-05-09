from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

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

post_detail_url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug',
    )

class PostListSerializer(ModelSerializer):
    url = post_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='posts-api:delete',
        lookup_field='slug',
    )
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            # 'slug',
            'content',
            'image',
            'html',
            'publish',
            'delete_url',
        ]
    def get_user(self,obj):
        return str(obj.user.username)

    def get_image(self,obj):
        try:
            image = obj.image.url
        except:
            return None
        return image

    def get_html(self,obj):
        return obj.get_markdown()

class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='posts-api:delete',
        lookup_field='slug',
    )
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'user',
            'title',
            'slug',
            'content',
            'image',
            'html',
            'publish',
            'delete_url',
        ]
    def get_user(self,obj):
        return str(obj.user.username)

    def get_image(self,obj):
        try:
            image = obj.image.url
        except:
            return None
        return image

    def get_html(self,obj):
        return obj.get_markdown()
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