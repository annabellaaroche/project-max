from django.contrib import admin
from .models import Owner,Especie,Raza,petSize,Pets,Vacuna,citaMedica
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserAdminConfig(UserAdmin):
    searh_fields = ('email','user_name','first_name')
    list_filter = ('email','user_name','first_name','is_active','is_staff')
    ordering = ('-start_date',)
    list_display = ('email','id','user_name','first_name','last_name','is_active','is_staff')
    fieldsets =(
        (None, {'fields': ('email','user_name','first_name','last_name',)}),
        ('Permissions', {'fields': ('is_staff','is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','user_name','id','first_name', 'last_name','password1','password2','is_active','is_staff')
        }),
    )
admin.site.register(Owner)
admin.site.register(Especie)
admin.site.register(Raza)
admin.site.register(petSize)
admin.site.register(Pets)
admin.site.register(Vacuna)
admin.site.register(citaMedica)
admin.site.register(NewUser, UserAdminConfig)