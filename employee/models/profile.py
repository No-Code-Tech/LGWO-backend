from django.db import models
from .country import Country
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


'''
Basic information about the employee
'''



User = get_user_model()




class EmployeeProfile(models.Model):


    class Status(models.TextChoices):
        JOINED = "JN",_("Joined")
        REGULAR = "RG",_("Regular")
        NOT_ASSIGNED = "NA",_("Not Assigned")

    user = models.OneToOneField(User,related_name="profile",on_delete=models.SET_NULL,null=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country,blank=True,null=True,on_delete=models.SET_NULL,related_name="country")
    contact_number = models.CharField(max_length=255)
    passport_size_photo = models.FileField(upload_to="employee/profile")
    status = models.CharField(
        max_length=10,
        choices=Status,
        default =Status.NOT_ASSIGNED
    )


    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    class Meta:
        app_label = 'employee'
    
