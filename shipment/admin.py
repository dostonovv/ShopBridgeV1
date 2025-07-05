from django.contrib import admin
from .models import Shipment

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'current_location', 'status', 'estimated_arrival', 'update_at')
    list_filter = ('status', 'update_at')
    search_fields = ('order__id', 'current_location')
    ordering = ('-update_at',)
