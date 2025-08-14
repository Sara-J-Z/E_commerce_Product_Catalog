from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Category
from main_app.models.product_model import Product
from main_app.models.brand_model import Brand
from main_app.models.newsletter_model import NewsletterSubscriber
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'gender')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'phone_number', 'address', 'gender')}),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)



class CategoryWithSubFilter(admin.SimpleListFilter):
    title = 'Category (with subcategories)'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        return [(cat.id, cat.name) for cat in Category.objects.filter(parent__isnull=True)]

    def get_subcategory_ids(self, parent_id):
        return list(Category.objects.filter(parent_id=parent_id).values_list('id', flat=True))

    def queryset(self, request, queryset):
        if self.value():
            category_id = int(self.value())
            child_ids = self.get_subcategory_ids(category_id)
            return queryset.filter(category__in=[category_id] + child_ids)
        return queryset


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price', 'quantity')
    search_fields = ('name',)
    list_filter = (CategoryWithSubFilter, 'brand')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)
    list_filter = ('parent',)

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at') 
    search_fields = ('email',) 
    list_filter = ('subscribed_at',)  
