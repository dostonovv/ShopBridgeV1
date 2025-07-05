# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:product_id>/', views.create_order_view, name='create_order'),
    path('my-orders/', views.order_list_view, name='order_list'),
    path('order/<int:pk>/', views.order_detail_view, name='order_detail'),
]
