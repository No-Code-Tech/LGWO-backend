from django.db import models
from .employee import Employee

class Document(models.Model):
    name = models.CharField(max_length=255)
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.name


    class Meta:
        app_label = "employee"

class EmployeeDocument(models.Model):
    document_type = models.ForeignKey(Document,related_name="document",on_delete=models.SET_NULL)
    employee = models.ForeignKey(Employee,related_name="employee",on_delete=models.CASCADE)
    file = models.FileField(upload_to="employee/documents")

    def __str__(self) -> str:
        return f"ID :{self.employee.id} Name :{self.employee.first_name} Document Name:{self.document.name}"

    class Meta:
        app_label = "employee"