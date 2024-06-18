from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_manager_name = models.CharField(max_length=100)
    contact_manager_email = models.EmailField(max_length=100)
    contact_manager_number = models.CharField(max_length=10)
    email = models.EmailField()
    number = models.CharField(max_length=10)


    def __str__(self):
        return self.name

    class Meta:
        app_label = "client"