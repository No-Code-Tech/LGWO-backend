from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import EmployeeTimeSheetVerification


# @receiver(post_save,sender=EmployeeTimeSheetVerification)
# def verification_handler(sender,instance,created,**kwargs):
#     if created:
#         time_sheet = instance.timesheet
#         time_sheet.is_verified = True
#         time_sheet.save()
        

