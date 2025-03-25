from rest_framework import serializers
from ..models import EmployeeProfile,Document
from .employee_timesheet import EmployeeTimeSheetSerializer
from .document import EmployeeDocumentSerializer
from user.models import CustomUser


class EmployeeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'mobile_number', 'password','username']
        extra_kwargs = {
            "password":{"write_only":True}
        }
    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.IID = CustomUser.objects.all().count()
        user.save()

        return user


class EmployeeTimeSheetField(serializers.RelatedField):
    def to_representation(self, value):
        timesheet = {
            "id":value.id,
            "duty_start_time":value.duty_start_time.strftime('%Y-%m-%d'),
            "total_duty_hours":value.total_duty_hours,
            "is_absent":value.is_absent,
            "client":value.client.name,
            "remark":value.remark
        }
        return timesheet
        # return EmployeeTimeSheetSerializer(value).data


class EmployeeDocumentField(serializers.RelatedField):
    def to_representation(self, value):

        document_info =  {
            "id":value.id,
            "type":{"value":value.document_type.id,"label":value.document_type.name},
            "url":value.file.url,
            "issued_date":value.issued_date,
            "expiry_date":value.expiry_date
        }

        return document_info
    
    
    def get_fields(self):
        fields = super().get_fields()
        return fields



class EmployeeProfileSerialier(serializers.ModelSerializer):

    class Meta:
        model = EmployeeProfile
        fields = '__all__'
    

class EmployeeDetailSerializer(serializers.ModelSerializer):

    timesheets = EmployeeTimeSheetField(many=True,read_only=True)
    documents = EmployeeDocumentField(many=True,read_only=True)
    surname = serializers.CharField(source="last_name")
    profile  = EmployeeProfileSerialier()
    
    class Meta:
        model = CustomUser
        fields = ("IID",'first_name',"surname","documents","mobile_number",'timesheets',"profile")


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['documents'].context.update(self.context)


    # def to_representation(self, instance):
    #     return super().to_representation(instance)


class EmployeeListSerializer(serializers.ModelSerializer):
    surname = serializers.CharField(source="last_name")

    class Meta: 
        model = CustomUser
        fields = ("IID",'first_name',"surname","mobile_number")








