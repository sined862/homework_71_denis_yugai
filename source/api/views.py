from rest_framework import generics, viewsets
from posts.models import Post
from accounts.models import Account
from api.serializers import PostSerializer, LikeSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer






class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AuthorSerializer