from django.db import models
from client.models.client import Client
from django.contrib.auth import get_user_model



User = get_user_model()
class TimeSheet(models.Model):
    drop_time = models.DateTimeField()
    drop_driver = models.ForeignKey(User,related_name="drop_driver",on_delete=models.SET_NULL,null=True)
    pickup_time = models.DateTimeField()
    pickup_driver = models.ForeignKey(User,related_name="pickup_driver",on_delete=models.SET_NULL,null=True)
    working_hours = models.PositiveIntegerField()
    client = models.ForeignKey(Client, on_delete=models.SET_NULL,null=True)
    department = models.CharField(max_length=100)
    duty_time = models.DateTimeField()
    duty_date = models.DateField()
    is_invoiced = models.BooleanField()


    def __str__(self):
        return f"{self.client.name} - {self.duty_time}"



    class Meta:
        app_label = "employee"






    
    

