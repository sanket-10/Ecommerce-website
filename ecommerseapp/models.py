from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    desc = models.TextField(max_length=500)
    phonenumber = models.IntegerField()

    def __str__(self):
        return str(self.email)


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default='')
    subcategory = models.CharField(max_length=50,default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/images',)

    def __str__(self):
        return str(self.product_name)