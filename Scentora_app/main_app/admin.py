from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Category


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

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)


