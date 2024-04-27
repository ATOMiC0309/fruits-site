from django.db import models


# Create your models here.
class Category(models.Model):
    """For category"""

    name = models.CharField(max_length=50, verbose_name='Category', unique=True)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created time")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated time")
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    published = models.BooleanField(default=True, verbose_name="Is published")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']


class Product(models.Model):
    """For product """

    name = models.CharField(max_length=150, verbose_name='Product')
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    quantity = models.IntegerField(default=0)
    color = models.CharField(max_length=20, blank=True, null=True)
    discount = models.FloatField(blank=True, null=True, default=0)
    slug = models.SlugField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created time")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated time")
    published = models.BooleanField(default=True, verbose_name="Is published")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
