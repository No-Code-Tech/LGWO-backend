from django.db import models

from .timesheet import TimeSheet
from django.contrib.auth import get_user_model




User = get_user_model()
class EmployeeTimeSheet(models.Model):
    employee = models.ForeignKey(User,related_name="timesheets",on_delete=models.SET_NULL,null=True)
    timesheet = models.ForeignKey(TimeSheet,related_name="time",on_delete=models.SET_NULL,null=True)
    duty_start_time = models.DateTimeField(blank=True,null=True)
    total_duty_hours = models.PositiveIntegerField(null=True,blank=True)
    rate = models.FloatField(blank=True,null=True)
    is_absent = models.BooleanField(blank=True,null=True)
    remark = models.TextField(blank=True,null=True)


    def __str__(self):
        return f"{self.employee} assigned - {self.timesheet.client} on {self.duty_start_time.strftime('%y-%m-%d')} - was " + ("absent" if self.is_absent else "present")
    class Meta:
        app_label = "employee"
        ordering = ["duty_start_time"]


