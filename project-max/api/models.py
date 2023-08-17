from django.db import models

# Create your models here.
 
class pets(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()


class Owner(models.Model):
    name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200)

