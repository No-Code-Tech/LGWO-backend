from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()
class Position(models.Model):
    name = models.CharField(max_length=100)
    job_description = models.TextField(blank=True)

    class Meta:
        app_label = "employee"

    def __str__(self):
        return self.name


class EmployeePosition(models.Model):
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    employee = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.employee.IID} {self.employee.first_name} {self.position.name}"

    class Meta:
        app_label = "employee"



