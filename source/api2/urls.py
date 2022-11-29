from django.urls import include, path
from rest_framework import routers
from api2 import views
from api2.views import LikeViewSet
from rest_framework.authtoken.views import obtain_auth_token



router = routers.DefaultRouter()
router.register(r'posts', views.ProductViewSet)

router_likes = routers.DefaultRouter()
router_likes.register(r'likes', LikeViewSet)
app_name = 'api2'

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router_likes.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]