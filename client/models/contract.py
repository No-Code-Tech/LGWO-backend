from django.db import models
from .client import Client


class Contract(models.Model):
    client = models.ForeignKey(Client,related_name="contracts",on_delete=models.SET_NULL,null=True)
    signed_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    is_terminated = models.BooleanField(default=False)
    is_terminate_date = models.DateField(null=True,blank=True)
    termination_reason = models.TextField(blank=True,null=True)
    document = models.FileField(upload_to="contract")
    
    def __str__(self):
        return f"{self.client.name} - {self.signed_date} - {self.expiry_date}"



    class Meta:
        app_label = "client"