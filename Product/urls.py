from django.urls import path

app_name = 'Product'

from .views import ProductList, ProductDetail

urlpatterns = [
    path('', ProductList.as_view(), name = 'product_list'),
    path('<slug:slug>', ProductDetail.as_view(), name = 'product_detail')
]
