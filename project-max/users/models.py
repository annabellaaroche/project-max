from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ #Library to transalate Json response or request like 'Email address'
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager#this let us override the default user table from django

# Create your models here.

#Users Model

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, user_name,first_name,password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email = email, user_name=user_name,first_name = first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, user_name,first_name,password, **other_fields):
            other_fields.setdefault('is_staff',True)
            other_fields.setdefault('is_superuser',True)
            other_fields.setdefault('is_active',True)
        
            if other_fields.get('is_staff') is not True:
                raise ValueError(
                    _('Superuser must be assigned to is_staff = True.')
                )
            if other_fields.get('is_superuser') is not True:
                raise ValueError(
                    _('Superuser must be assigned to is_superuser = True.')
                )
            return self.create_user(email,user_name,first_name,password, **other_fields)    

class NewUser(AbstractBaseUser,PermissionsMixin):

    id= models.AutoField(primary_key=True,unique=True)
    email= models.EmailField(_('email address'),unique=True)
    user_name = models.CharField(max_length=150,unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) #Add Other authentication later

    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name']

    def __str__(self):
        return self.user_name

