from django.db import models
from django.conf import settings

# Create your models here.
class Especie(models.Model):

    id_especie = models.AutoField(primary_key=True,unique=True)
    name_especie = models.CharField(max_length=100)

class Raza(models.Model):
    id_raza = models.AutoField(primary_key=True, unique=True)
    name_raza=models.CharField(max_length=100)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)

class petSize(models.Model):
    id_pet_size = models.AutoField(primary_key=True,unique=True)
    name_tamano = models.CharField(max_length=50)

class Owner(models.Model):
    name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200)

class Pets(models.Model):
    id_pet = models.AutoField(primary_key=True, unique=True)
    name_pet = models.CharField(max_length=100)
    birth_date_pet = models.DateField()
    raza_id = models.ForeignKey(Raza,on_delete=models.CASCADE)
    pet_size_id=models.ForeignKey(petSize,on_delete=models.CASCADE)
    pet_gender = models.CharField(max_length=10) #F or M
    pet_color = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)

class Vacuna(models.Model):
    id_vacuna = models.AutoField(primary_key=True,unique=True)
    name_vacuna = models.CharField(max_length=100)
    date_vacuna = models.DateField()
    next_vacuna_date = models.DateField()
    mascota = models.ForeignKey(Pets,on_delete=models.CASCADE)

class citaMedica(models.Model):
    id_cita = models.AutoField(primary_key=True,unique=True)
    fecha_cita = models.DateField()
    motivo_cita=models.CharField(max_length=100)
    notas_cita = models.TextField()
    mascota= models.ForeignKey(Pets,on_delete=models.CASCADE)



