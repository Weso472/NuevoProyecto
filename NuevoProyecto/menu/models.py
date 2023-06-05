from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(null=True)
    image = models.ImageField(upload_to='menu_photos', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):             #esto se hace para que en /admin aparezca el nombre del objeto y no "Product object(1)""
        return self.title