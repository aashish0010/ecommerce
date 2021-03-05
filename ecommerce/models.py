from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Cat, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000, default='')
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default='')

    def __str__(self):
        return self.name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    area = models.TextField(max_length=2000)

    def __str__(self):
        return self.email

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    itemsJson = models.CharField(max_length=2000)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=222)
    zip_code = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.name

