from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Store(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100,  null=True)
    email = models.EmailField(max_length=100,  null=True)
    city = models.CharField(max_length=100,  null=True)
    state = models.CharField(max_length=100,  null=True)
    zip_code = models.CharField(max_length=100,  null=True)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200,  null=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add =True, null=True)
    date_expired = models.DateTimeField(null=True)
    price = models.FloatField(null=True)
    

class Stock(models.Model):
    store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True)
    quantity = models.IntegerField(null=True)
    