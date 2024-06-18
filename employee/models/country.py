from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100,verbose_name="Country Name")
    code = models.CharField(max_length=2,verbose_name="Country Code")   

    def __str__(self):
        return self.name

    class Meta:
        app_label = "employee"