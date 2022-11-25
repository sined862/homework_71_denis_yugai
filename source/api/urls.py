from django.urls import path, include
from api.views import PostAPIView, PostViewSet
from rest_framework import routers

posts_router = routers.SimpleRouter()
posts_router.register(r'posts', PostViewSet)
urlpatterns = [
    path('', include(posts_router.urls))
]