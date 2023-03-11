from django.contrib import admin

# Register your models here.
from .models import Order, Order_Detail, Cart, Cart_Detail


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_code','order_status','order_date','order_date']
    list_filter = ['order_status','order_date']

class Order_DetailAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity','total']
    list_filter = ['price','quantity']


admin.site.register(Order, OrderAdmin)
admin.site.register(Order_Detail, Order_DetailAdmin)
admin.site.register(Cart)
admin.site.register(Cart_Detail)
