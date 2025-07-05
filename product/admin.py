from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'seller', 'created_at')
    list_filter = ('created_at', 'seller')
    search_fields = ('name', 'seller__username')
    ordering = ('-created_at',)
