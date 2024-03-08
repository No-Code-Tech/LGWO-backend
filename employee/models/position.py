from django.db import models
from employee import Employee

class Position(models.Model):
    name = models.CharField(max_length=100)
    job_description = models.TextField(blank=True)

    class Meta:
        app_label = "employee"


class EmployeePosition(models.Model):
    position = models.OneToOneField(Position,related_name="position",on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name="employee",on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.employee.id} {self.employee.first_name} {self.position.name}"

    class Meta:
        app_label = "employee"



