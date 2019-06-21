from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Product(models.Model):

    seller = models.TextField(default='Unknown Seller')
    product_name = models.TextField(default='Unknown Name')
    product_price_AUD = models.FloatField(default=0)
    product_price_TWD = models.FloatField(default=0)
    pre_selling_price_AUD = models.FloatField(default=0)
    pre_selling_price_TWD = models.FloatField(default=0)
    actual_selling_price_AUD = models.FloatField(default=0)
    actual_selling_price_TWD = models.FloatField(default=0)
    description = models.TextField(default='Unknown Description')

    class Meta:
        db_table = 'product'
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})


