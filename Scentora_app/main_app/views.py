from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .models import CustomUser, Category, Product, Brand
from .models.newsletter_model import NewsletterSubscriber
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import JsonResponse
from rest_framework import generics
from .serializers import (
    ProductSerializer, 
    BrandSerializer, 
    BrandDetailSerializer,
    CustomUserSerializer, 
    CategorySerializer, 
    RegisterSerializer,
    CustomTokenObtainPairSerializer,
    NewsletterSubscriberSerializer
)



# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BrandDetailSerializer
        return BrandSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer

    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(RegisterSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def test_users_endpoint(request):
    return JsonResponse({"message": "Users endpoint is working"})

class SignInView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        print(user)
        if user:
            print("before token")
            token = CustomTokenObtainPairSerializer.get_token(user=user)
            print(token)
            return Response({
                'token': str(token),
                'user_id': user.id,
                'email': user.email
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)
    
class NewsletterSubscriberCreateView(generics.CreateAPIView):
        queryset = NewsletterSubscriber.objects.all()
        serializer_class = NewsletterSubscriberSerializer









