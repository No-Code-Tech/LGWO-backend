from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _


from django.contrib.auth import get_user_model
from client.models import Client



User = get_user_model()
class EmployeeTimeSheet(models.Model):

    class Status(models.TextChoices):
        ROSTER = "ROSTER",_("Roster")
        SUPERVISOR = "SUPERVISOR",_("Supervisor")
        IN_PROCESS = "IN_PROCESS",_("In Process")
        VERIFIED = "VERIFIED",_("Verified")



    employee = models.ForeignKey(User,related_name="timesheets",on_delete=models.SET_NULL,null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL,null=True)
    department = models.CharField(max_length=100,null=True,blank=True)
    duty_start_time = models.DateTimeField(blank=True,null=True)
    total_duty_hours = models.PositiveIntegerField(null=True,blank=True)
    rate = models.FloatField(blank=True,null=True)
    is_absent = models.BooleanField(blank=True,null=True)
    remark = models.TextField(blank=True,null=True)
    is_verified = models.BooleanField(blank=True,null=True,default=False)
    verification_status = models.CharField(
        max_length=10,
        choices=Status,
        default =Status.ROSTER
    )    
    is_invoiced = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.employee} assigned - {self.client} on {self.duty_start_time.strftime('%y-%m-%d')} - was " + ("absent" if self.is_absent else "present")
    class Meta:
        app_label = "employee"
        ordering = ["duty_start_time"]


'''
Verification precedence
    Admin->Manager->Team Leader (verified by Team Leader should be verified by Manager as well)
'''
                        
class EmployeeTimeSheetVerification(models.Model):
    timesheet = models.ForeignKey(EmployeeTimeSheet,related_name="logs",verbose_name="Employee TimeSheet",on_delete=models.SET_NULL,null=True)
    verified_by = models.ForeignKey(User,related_name="verified",on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.verified_by.email


class TimeSheetChangeLog(models.Model):
    timesheet = models.ForeignKey('EmployeeTimeSheet', on_delete=models.CASCADE, related_name='change_logs')
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    changed_at = models.DateTimeField(auto_now_add=True)
    field_name = models.CharField(max_length=100)
    old_value = models.TextField(null=True)
    new_value = models.TextField()

    def __str__(self):
        return f"Change to {self.timesheet} - {self.field_name} by {self.changed_by}"

@receiver(pre_save, sender=EmployeeTimeSheet)
def log_timesheet_changes(sender, instance, **kwargs):
    if instance.pk:  # This check ensures that we're updating an existing instance, not creating a new one
        old_instance = EmployeeTimeSheet.objects.get(pk=instance.pk)
        for field in EmployeeTimeSheet._meta.fields:
            old_value = getattr(old_instance, field.name)
            new_value = getattr(instance, field.name)
            if old_value != new_value:
                # Handle foreign key and date fields
                if isinstance(field, (models.ForeignKey, models.DateTimeField, models.DateField)):
                    old_value = str(old_value)
                    new_value = str(new_value)
                
                TimeSheetChangeLog.objects.create(
                    timesheet=instance,
                    changed_by=instance.last_modified_by if hasattr(instance, 'last_modified_by') else None,
                    field_name=field.name,
                    old_value=old_value,
                    new_value=new_value
                )

