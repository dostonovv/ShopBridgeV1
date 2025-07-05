from django.shortcuts import render, redirect , get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
@login_required
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('product_list')  # yoki boshqa sahifaga
    else:
        form = ProductForm()
    return render(request, 'product/create_product.html', context={'form': form})

def product_list_view(request):
    products = Product.objects.all().order_by('-id')  # Eng oxirgi mahsulotlar birinchi bo‘ladi
    return render(request, 'product/product_list.html', context={'products': products})

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})

