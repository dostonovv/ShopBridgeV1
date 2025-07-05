from django.db import models

from accounts.models import User

class Product(models.Model):
    """model"""

    name = models.CharField(max_length=35)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User , on_delete=models.CASCADE , related_name='product')
    # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    image1 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='product_images/', null=True, blank=True)

class Meta:
    ordering = ['-created_at']
    verbose_name = 'Mahsulot'
    verbose_name_plural = 'Mahsulotlar'