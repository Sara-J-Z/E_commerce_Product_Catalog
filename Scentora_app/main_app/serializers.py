from rest_framework import serializers
from main_app.models.product_model import Product
from main_app.models.brand_model import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'logo']  
        
class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    # category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), source='brand', write_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'quantity', 
                  'category', 'brand', 'category_id', 'brand_id', 'created_at']
    


