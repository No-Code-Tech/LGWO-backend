from django.db import models
from .client import Client

class CasualOrder(models.Model):
    client = models.ForeignKey(Client,on_delete=models.SET_NULL)
    by = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    medium = models.CharField(max_length=100)


    class Meta:
        app_label = "client"
    

