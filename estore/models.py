from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    PRODUCT_CATEGORIES = (
        ('MP', 'Mobile Phones'),
        ('MAC', 'Apple Mac'),
        ('PC', 'PC'),
        ('GC', 'Game Consoles')
    )
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length= 500, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(choices=PRODUCT_CATEGORIES, max_length=10, null=True)

    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except :
            url = ''
        return url

class Category(models.Model):
    title = models.CharField(Product.category, max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    ORDER_STATUS = (
        ('P', 'Pending'),
        ('AD', 'At Delivery'),
        ('D', 'Delivered')
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    id_order = models.CharField(max_length=100, null=True)
    status = models.CharField(choices=ORDER_STATUS, max_length=15, null=True, )

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank= True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    zipcode = models.CharField(max_length=7, null=True)
    country = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.address

