from rest_framework import serializers
from posts.models import Post
from accounts.models import Account


class UserLikesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name', 'liked_posts')


class PostSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'description', 'image', 'author')
        read_only_fields = ['author']




