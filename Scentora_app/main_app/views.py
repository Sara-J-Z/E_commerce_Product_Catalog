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
