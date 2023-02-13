from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Count
from .models import Product, Brand

# Create your views here.


class ProductList(ListView):
    model= Product
    paginate_by=1

class ProductDetail(DetailView):
    model= Product



class BrandList(ListView):
    paginate_by=1
    model=Brand
    queryset=Brand.objects.all().annotate(product_count=Count('product_brand'))

class BrandDSingle(ListView):
    model=Brand
    #queryset=Brand.objects.filter().annotate(product_count=Count('product_brand'))

    def get_queryset(self):
        queryset = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))
        return queryset
    