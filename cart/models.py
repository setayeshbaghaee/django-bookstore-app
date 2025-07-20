from django.db import models
from accounts.models import User
from store.models import Book

class Cart (models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        return sum(item.get_total_price() for item in self.items.all())
    
    def get_total_items(self):
        return sum(item.quantity for item in self.items.all())
    def __str__(self):
        return f"{self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} x {self.product.title} in Cart {self.cart.id}"

    def get_total_price(self):
        return self.quantity * self.product.price
