import cart as cart
from django.db import models
from shop.models import product

# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True,null=True)
    date_added=models.DateField(auto_now_add=True)
    class Meta:
        db_table='Cart'
        ordering=['date_added']
    def __str__(self):
        return '{}'.format(self.cart_id)

class CartItem(models.Model):
    products=models.ForeignKey(product,on_delete=models.CASCADE,default=None, null=True, editable=False)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,default=None, null=True, editable=False)
    quantity=models.IntegerField(null=True)
    active=models.BooleanField(default=True)
    class Meta:
        db_table='CartItem'
    def sub_total(self):
        return self.products.price * self.quantity
    def __str__(self):
        return '{}'.format(self.products)

