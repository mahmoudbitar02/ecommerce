from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Count
from .models import Product, Brand

# Create your views here.


class ProductList(ListView):
    model= Product
    paginate_by=50

class ProductDetail(DetailView):
    model= Product



class BrandList(ListView):
    paginate_by=50
    model=Brand
    queryset=Brand.objects.all().annotate(product_count=Count('product_brand'))

class BrandDSingle(ListView):
    model=Product
    paginate_by=50
    template_name= 'Product/brand_single.html'
   

    def get_queryset(self):
        
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        data=Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        context["brand"] = data
        return context
    