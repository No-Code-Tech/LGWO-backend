from django.db import models
from employee import Employee
from timesheet import TimeSheet

class EmployeeTimeSheet(models.Model):
    employee = models.ForeignKey(Employee,related="employee",on_delete=models.SET_NULL)
    timesheet = models.ForeignKey(TimeSheet,related="timesheet",on_delete=models.SET_NULL)
    duty_start_time = models.DateTimeField(blank=True,null=True)
    total_duty_hours = models.PositiveIntegerField(null=True,blank=True)
    rate = models.FloatField(blank=True,null=True)
    is_absent = models.BooleanField(blank=True,null=True)
    remark = models.TextField(blank=True,null=True)



    class Meta:
        app_label = "employee"

