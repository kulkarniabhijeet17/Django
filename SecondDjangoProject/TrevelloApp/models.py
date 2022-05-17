from django.db import models

# Create your models here.

class destination1:
    id: int
    name: str
    img: str
    description: str
    price: str
    offer: bool

class destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics', null=True)
    description = models.TextField(null=True)
    price = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)