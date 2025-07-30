from rest_framework import serializers
from rest_framework import serializers
from .models import CustomUser, Category

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'email', 'username', 'date_of_birth', 'phone_number',
            'address', 'gender'
        ]
        # You can add extra kwargs if needed, e.g. read_only_fields = ['id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'is_active']
