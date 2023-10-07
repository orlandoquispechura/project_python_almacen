from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        blank=False
    )
    description = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.name.upper()


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    stock = models.IntegerField(default=0, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=True)
    dni = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name


class Sale(models.Model):
    date_sale = models.DateTimeField(blank=True, auto_now_add=True)
    status = models.BooleanField(default=True, blank=True)
    total = models.DecimalField(decimal_places=2, max_digits=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="DetailSale", blank=True)


class DetailSale(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price_sale = models.DecimalField(decimal_places=2, max_digits=10)
