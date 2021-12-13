from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from pprint import pprint

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.user.username
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="images/")
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    AVAILABILITY_CHOICES = [
        (0, 'NO'),
        (1, 'YES'),
    ]
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images/")
    availability = models.SmallIntegerField(choices=AVAILABILITY_CHOICES, default=1)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.product.name

    # class Meta:
    #     unique_together = [['cart', 'product']]

    def save(self, *args, **kwargs):
        if self._state.adding:
            try:
                cart_item = CartItem.objects.get(cart_id=self.cart.id, product_id=self.product.id)
                quantity = cart_item.quantity + int(self.quantity)              
                CartItem.objects.filter(pk=cart_item.id).update(quantity=quantity)
            except CartItem.DoesNotExist:
                super(CartItem, self).save(*args, **kwargs)
        else:
            super(CartItem, self).save(*args, **kwargs)

