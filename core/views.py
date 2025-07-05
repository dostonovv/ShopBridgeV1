from django.shortcuts import render
from product.models import Product  # product appdan modelni import qilamiz

def home_view(request):
    products = Product.objects.all().order_by('-id')  # eng oxirgi mahsulotlar birinchi
    return render(request, 'home.html', {'products': products})
