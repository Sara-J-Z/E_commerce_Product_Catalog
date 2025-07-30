from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser, Category
from .serializers import CustomUserSerializer, CategorySerializer

# Create your views here.

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
