from django.db import models

# Create your models here.

"""
Product
     Nom
     Prix
     quantité
     descrition
     image
"""

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} ({self.stock})"