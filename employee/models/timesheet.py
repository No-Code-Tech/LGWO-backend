from django.db import models
from employee import Employee
from ...client.models.client import Client

class TimeSheet(models.Model):
    drop_time = models.DateTimeField()
    drop_driver = models.ForeignKey(Employee,on_delete=models.NULL)
    pickup_time = models.DateTimeField()
    pickup_driver = models.ForeignKey(Employee,on_delete=models.NULL)
    working_hours = models.PositiveIntegerField()
    client = models.ForeignKey(Client, on_delete=models.NULL)
    department = models.CharField(max_length=100)
    duty_time = models.DateTimeField()
    duty_date = models.DateField()
    is_invoiced = models.BooleanField()



    class Meta:
        app_label = "employee"






    
    

