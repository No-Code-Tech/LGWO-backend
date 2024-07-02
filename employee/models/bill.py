from django.db import models

class Bill(models.Model):
    number = models.CharField(max_length=10000,primary_key = True,verbose_name="Work No.")



    def __str__(self):
        return self.number

    class Meta: 
        app_label = "employee"