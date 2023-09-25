from rest_framework import serializers
from .models import Owner,Especie,Raza,petSize,Pets,Vacuna,citaMedica

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('id','name','phone','email','address')
        #read_only_fields = ('id')

class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = ('id_especie','name_especie')

class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = ('id_raza','name_raza','especie')

class petSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = petSize
        fields = ('id_pet_size','name_tamano')

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = ('id_pet','name_pet','birth_date_pet','raza_id','pet_size_id','pet_gender','pet_color','owner')

class VacunaSerializer(serializers.ModelSerializer):
    mascota = PetsSerializer()
    class Meta:
        model = Vacuna
        fields = ('id_vacuna','name_vacuna','date_vacuna','next_vacuna_date','mascota')

class VacunaSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ('id_vacuna','name_vacuna','date_vacuna','next_vacuna_date','mascota')        

class citaMedicaSerializer(serializers.ModelSerializer):
    mascota = PetsSerializer()
    class Meta:
        model = citaMedica
        fields = ('id_cita','fecha_cita','motivo_cita','notas_cita','mascota')
       
class citaMedicaSerializer2(serializers.ModelSerializer):
    class Meta:
        model = citaMedica
        fields = ('id_cita','fecha_cita','motivo_cita','notas_cita','mascota')