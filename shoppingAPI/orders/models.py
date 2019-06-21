from django.db import models
from products.models import Product
# Create your models here.


class Order(models.Model):
    
    orderDate = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product)
    totalPrice = models.FloatField(default=0)
    buyer = models.TextField(default='Unknow Buyer')
    deliverDate = models.TextField(default= 'Unknown Date')


    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Order_detail", kwargs={"pk": self.pk})
