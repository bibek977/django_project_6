from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'products')
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    description = models.TextField()
    warrenty = models.CharField(max_length=200, null=True, blank=True)
    return_policy = models.CharField(max_length=200, null=True, blank=True)
    view_count = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.title

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    total = models.PositiveIntegerField(default = 0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart : " + str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Cart : " + str(self.cart.id) + "Cart Product : " + str(self.id)


ORDER_STATUS = (
    ("order received", "order received"),
    ("order processing", "order processing"),
    ("order on the way", "order on the way"),
    ("order completed", "order completed"),
    ("order canceled", "order canceled"),
)

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order : " + str(self.id)