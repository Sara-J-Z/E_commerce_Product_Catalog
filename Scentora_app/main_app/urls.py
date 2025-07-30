from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from .views import ProductViewSet, BrandViewSet
=======
from .views import CustomUserViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')
>>>>>>> 228aec9ea0d355367b7f6dc29d07343c8e4886e2

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'brands', BrandViewSet)

urlpatterns = [
<<<<<<< HEAD
path('api/', include(router.urls)),
=======
    path('api/', include(router.urls)),
   
>>>>>>> 228aec9ea0d355367b7f6dc29d07343c8e4886e2
]


