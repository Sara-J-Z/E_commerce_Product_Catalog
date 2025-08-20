
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    ProductViewSet,
    BrandViewSet,
    CustomUserViewSet,
    CategoryViewSet,
    CustomTokenObtainPairView,
    test_users_endpoint,
    CategoryDetailView,
    ProfileView,
    RegisterView,
    PasswordUpdateView
    # SignInView
    
)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet)
router.register(r'brands', BrandViewSet)

urlpatterns = [
    path('test_users/', test_users_endpoint, name='test_users'),
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update-password/', PasswordUpdateView.as_view(), name='update_password'),
    path('signin/', CustomTokenObtainPairView.as_view(), name='signin'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]


