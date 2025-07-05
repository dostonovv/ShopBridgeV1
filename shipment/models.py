from django.db import models

class Shipment(models.Model):
    """state delivery"""
    order = models.ForeignKey('orders.Orders' , on_delete=models.CASCADE)
    current_location = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ('china_warehouse', 'Xitoy omborida'),
            ('on_the_way', 'Yo‘lda'),
            ('customs', 'Bojxonada'),
            ('local_delivery', 'Mahalliy yetkazish'),
            ('delivered', 'Yetkazildi')
        ],
        default='china_warehouse'
    )
    estimated_arrival = models.DateField(null=True , blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
