from django.urls import path, include, re_path
from api.views import LikeViewSet, PostViewSet
from rest_framework import routers

posts_router = routers.SimpleRouter()
posts_router.register(r'posts', PostViewSet)

likes_router = routers.SimpleRouter()
likes_router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(posts_router.urls)),
    path('', include(likes_router.urls)),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]