from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Cart, Cart_Detail, Order, Order_Detail


# Create your views here.

class OrderList(ListView):
    model = Order
    context_object_name = 'orders'

    paginate_by=1
