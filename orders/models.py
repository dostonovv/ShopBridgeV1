from django.db import models
from product.models import Product
from accounts.models import User

class Orders(models.Model):
    """models uchun model"""
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    customer = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
