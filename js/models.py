from django.db import models

# Create your models here.
class Product_1(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    qty = models.IntegerField()

    class Meta():
        db_table = 'product_1'


