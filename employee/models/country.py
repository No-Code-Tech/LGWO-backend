from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)   

    def __str__(self):
        return self.name

    class Meta:
        app_label = "country"