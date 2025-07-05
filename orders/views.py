# orders/views.py
from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from .models import Orders
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

@login_required
def create_order_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            Orders.objects.create(
                product=product,
                customer=request.user,
                quantity=quantity
            )
            return redirect('home')  # yoki boshqa sahifa
    else:
        form = OrderForm()

    return render(request, 'orders/create_order.html', {
        'form': form,
        'product': product
    })
@login_required
def order_list_view(request):
    orders = Orders.objects.filter(customer=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def order_detail_view(request, pk):
    order = get_object_or_404(Orders, pk=pk, customer=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})
