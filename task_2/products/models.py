from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='subcategories/')
    parent_category = models.ForeignKey(
        Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image_small = models.ImageField(upload_to='products/small/')
    image_medium = models.ImageField(upload_to='products/medium/')
    image_large = models.ImageField(upload_to='products/large/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(
        SubCategory, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
