from django.urls import path
from posts.views import IndexView, PostAddView, PostDetail


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('posts/post_add', PostAddView.as_view(), name='post_add'),
    path('posts/post/<int:pk>', PostDetail.as_view(), name='post')
]