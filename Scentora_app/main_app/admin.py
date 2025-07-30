from django.contrib import admin

from main_app.models.product_model import Product
from main_app.models.brand_model import Brand
# Register your models here.

admin.site.register(Product)
admin.site.register(Brand)
