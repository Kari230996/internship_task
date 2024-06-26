from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class CartItem(models.Model):
    user = models.ForeignKey(
        User, related_name='cart_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
