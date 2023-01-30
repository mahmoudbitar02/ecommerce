from django.db import models
from django.utils import timezone
from Product.models import Product

# Create your models here.

ORDER_STATUS= (
    ('Resieved','Resieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)

class Order(models.Model):
    order_code = models.CharField(max_length=10)
    user=''
    order_status=models.CharField(max_length=15, choices=ORDER_STATUS, default='Resieved')
    delevery_date=models.DateTimeField(null= True, blank=True)
    order_date=models.DateTimeField(default= timezone.now)



class Order_Detail(models.Model):
    Order=models.ForeignKey(Order, related_name='order_detail', on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='order_product', on_delete=models.SET_NULL, null=True, blank=True)