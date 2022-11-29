from django.shortcuts import render
from api2.serializers import *
from api2.views import *
from rest_framework import viewsets
from accounts.models import Account




class ProductViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerialiazer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = UserLikesSerilizer