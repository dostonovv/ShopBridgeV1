from django.urls import path
from .views import product_create_view , product_list_view , product_detail_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', product_create_view, name='product_create'),
    path('list/', product_list_view, name='product_list'),
    path('<int:pk>/', product_detail_view, name='product_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
