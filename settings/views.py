from django.shortcuts import render
from .models import Company
from Product.models import Product, Brand, Reviews
from django.db.models import Count


def home(request):
    brands = Brand.objects.all().annotate(product_count=Count('product_brand'))
    items_sale= Product.objects.filter(flag='Sale')[:10]
    items_feature= Product.objects.filter(flag='Feature')[:6]
    items_new= Product.objects.filter(flag='New')[:12]
    reviews = Reviews.objects.all()[:6]
    return render(request,'settings/home.html',{
        'brands':brands,
        'items_sale':items_sale,
        'items_feature':items_feature,
        'items_new':items_new,
        'reviews':reviews,
    })


