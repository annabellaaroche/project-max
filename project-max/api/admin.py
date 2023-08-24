from django.contrib import admin
from .models import Owner,Especie,Raza,petSize,Pets,Vacuna,citaMedica


# Register your models here.

admin.site.register(Owner)
admin.site.register(Especie)
admin.site.register(Raza)
admin.site.register(petSize)
admin.site.register(Pets)
admin.site.register(Vacuna)
admin.site.register(citaMedica)