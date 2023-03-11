from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Product, Brand
from django.db.models import Q,F, Value, Func, ExpressionWrapper, DecimalField,FloatField 
from django.db.models import Sum, Avg, Min, Max, Count 
from django.db.models.functions import Concat
from .forms import ProductReviewForm
# Create your views here.


def query_Debug(request):
    #data = Product.objects.filter(name__contains='Noah', price__lt=75)
    #data = Product.objects.filter(Q(name__contains='Noah') & Q(price__lt=75))
    #data = Product.objects.filter(price= F('quantity'))
    #data = Product.objects.filter(price__lt=75).order_by('name',).reverse()
    #data = Product.objects.order_by('name')
    #data = Product.objects.select_related('brand').all()
    #data = Product.objects.predetch_related('brand').all() # many to many

    #data= Product.objects.annotate(
     #   Full_name= Func(F('name'),F('flag'), function='CONCAT')
    
    #)

    #data= Product.objects.annotate(
     #   Full_name= Concat('name',Value(' '), 'flag')
    
    #)
    dis_price=ExpressionWrapper(F('price')*.8,output_field=DecimalField())
    data=Product.objects.annotate(discounted_price = dis_price)

    return render (request,'Product/productlist.html',{'data':data})


class ProductList(ListView):
    model= Product
    paginate_by=50

class ProductDetail(DetailView):
    model= Product


def add_review(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user 
            myform.product = product
            myform.save()
    return redirect(f'/products/{product.slug}')



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
    