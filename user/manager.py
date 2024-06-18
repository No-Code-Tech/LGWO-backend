from django.contrib.auth.models import BaseUserManager
from django.db import models




class CustomUserManager(BaseUserManager):
    def create_user(self,password,**extra_fields):


        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(password=password, **extra_fields)


        