from django.contrib import admin
from .models import Orders

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'quantity', 'created_at')
    list_filter = ('created_at', 'product')
    search_fields = ('customer__username', 'product__name')
    ordering = ('-created_at',)
