from django.db import models
from django.utils import timezone
from Product.models import Product
from django.contrib.auth.models import User
from utils.generate_code import generate_code

# Create your models here.

ORDER_STATUS= (
    ('Resieved','Resieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)

class Order(models.Model):
    order_code = models.CharField(max_length=10, default= generate_code)
    user=models.ForeignKey(User, related_name='user_order', on_delete= models.SET_NULL, null=True, blank=True)
    order_status=models.CharField(max_length=15, choices=ORDER_STATUS, default='Resieved')
    delevery_date=models.DateTimeField(null= True, blank=True)
    order_date=models.DateTimeField(default= timezone.now)
    def __str__(self):
        return self.order_code



class Order_Detail(models.Model):
    order=models.ForeignKey(Order, related_name='order_detail', on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='order_product', on_delete=models.SET_NULL, null=True, blank=True)
    price= models.FloatField()
    quantity =models.IntegerField(default=1)
    total= models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.order)
    
    def save(self, *args, **kwargs):
       self.total=self.price * self.quantity
       super(Order_Detail, self).save(*args, **kwargs) # Call the real save() method