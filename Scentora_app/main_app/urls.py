from django.urls import path, include
from .views import test_users_endpoint 
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    ProductViewSet,
    BrandViewSet,
    CustomUserViewSet,
    CategoryViewSet,
    CustomTokenObtainPairView,
    RegisterView,
    SignInView,
    CategoryDetailView,
    NewsletterSubscriberCreateView,

)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet)
router.register(r'brands', BrandViewSet)

urlpatterns = [
    path('users/test/', test_users_endpoint),
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('newsletter/subscribe/', NewsletterSubscriberCreateView.as_view(), name='newsletter-subscribe'),

]


