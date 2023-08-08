from django.db import models
from store.models import Cart, Product

class CartItem(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()