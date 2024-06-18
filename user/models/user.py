from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from django.db import models
from django.utils import timezone
from ..manager import CustomUserManager

class CustomUser(AbstractUser):
    IID = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    mobile_number = models.CharField(max_length=30, unique=True)

    
    USERNAME_FIELD = 'IID'

    objects = CustomUserManager()



    def __str__(self):
        return self.IID




