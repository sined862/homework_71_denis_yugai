from django.urls import path
from posts.views import IndexView, PostAddView, PostDetail, AccountsListView, AccountDetailView, SubscribeView
from posts.views import LikeView
from accounts.views import is_autorization


urlpatterns = [
    path('posts/', IndexView.as_view(), name='index'),
    path('', is_autorization, name='is_autorization'),
    path('posts/post_add', PostAddView.as_view(), name='post_add'),
    path('posts/post/<int:pk>', PostDetail.as_view(), name='post'),
    path('posts/post/like/<int:pk>', LikeView.as_view(), name='like'),
    path('posts/post/comment', PostDetail.as_view(), name='comment_add'),
    path('search/', AccountsListView.as_view(), name='search'),
    path('accounts/account/<int:pk>', AccountDetailView.as_view(), name='account'),
    path('accounts/account/subscribe/<int:pk>', SubscribeView.as_view(), name='subscribe'),
]