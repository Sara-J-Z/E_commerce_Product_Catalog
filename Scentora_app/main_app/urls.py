from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')


urlpatterns = [
    path('api/', include(router.urls)),
   
]


