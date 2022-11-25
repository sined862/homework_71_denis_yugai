from rest_framework import serializers
from posts.models import Post
from accounts.models import Account


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','description', 'author', 'image')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email','liked_posts',)

class LikeSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(source='user_likes')
    class Meta:
        model = Post
        fields = ('id', 'authors')