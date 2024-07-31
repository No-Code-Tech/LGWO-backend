from django.db import models
from django.contrib.auth import get_user_model


'''
This log include every action of and employee which includes Traing Period, Joining Time, Leaving Status, Complain From Hotel
'''


User = get_user_model()

class Cycle(models.Model):
    order = models.IntegerField(verbose_name="Order")
    name = models.CharField(max_length=100,verbose_name="Cycle Name")
    description = models.TextField(blank=True)



class EmployeeCycle(models.Model):
    employee = models.ForeignKey(User,related_name="cycles",on_delete=models.SET_NULL,null=True)
    cycle = models.ForeignKey(Cycle,related_name="cycle",on_delete=models.SET_NULL,null=True)


class EmplpoyeeLog(models.Model):
    employee = models.ForeignKey(User,related_name="logs",on_delete=models.SET_NULL,null=True)
    info = models.CharField(max_length=100)
    



    
