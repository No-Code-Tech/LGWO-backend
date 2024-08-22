from django.db import models

from django.contrib.auth import get_user_model
from src.utils.storage_file import FileStorage


User = get_user_model()
class Document(models.Model):
    name = models.CharField(max_length=255)
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.name


    class Meta:
        app_label = "employee"

class EmployeeDocument(models.Model):
    document_type = models.ForeignKey(Document,on_delete=models.SET_NULL,null=True,verbose_name="Document Name")
    employee = models.ForeignKey(User,related_name="documents",on_delete=models.CASCADE,null=True)
    # file = models.FileField(upload_to="employee/documents")
    file = models.FileField(storage=FileStorage())
    issued_date = models.DateField(null=True,blank=True)
    expiry_date = models.DateField(null=True,blank=True)
    is_valid = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        self.is_valid = True
        super().save(*args,**kwargs)

    def __str__(self) -> str:
        return f"ID :{self.employee.id} Name :{self.employee.first_name} Document Name:{self.document_type.name}"

    class Meta:
        app_label = "employee"