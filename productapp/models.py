from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product_cart(models.Model):
    cart= models.ForeignKey('Shopping_cart', on_delete=models.CASCADE)
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_link= models.CharField(max_length=500)
    brand= models.CharField(max_length=255)
    size = models.CharField(
        max_length=1,
        choices=SIZE_CHOICES,
        blank=True,
        null=True,
    )
    quantity= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_price(self):
        return self.quantity * self.price

    class Meta:
            db_table= "Products for carts"

class Shopping_cart(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    product_list= models.ManyToManyField(Product_cart)

    class Meta:
        db_table = "Shopping_carts"



