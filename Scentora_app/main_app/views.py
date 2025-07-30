from django.shortcuts import render
from rest_framework import viewsets
from main_app.models.product_model import Product
from main_app.models.brand_model import Brand
from .serializers import ProductSerializer, BrandSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

from .models import CustomUser, Category
from .serializers import CustomUserSerializer, CategorySerializer

# Create your views here.

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

