from django.db import models
from .country import Country

'''
Basic information about the employee
'''

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CHARField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255)
    country = models.OneToOneField(Country,blank=True,null=True,on_delete=models.SET_NULL)
    contact_number = models.CharField(max_length=255)
    passport_size_photo = models.FileField(upload_to="employee/profile")


    class Meta:
        app_label = 'employee'
    
