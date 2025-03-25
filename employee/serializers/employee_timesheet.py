from rest_framework import serializers
from ..models import EmployeeTimeSheet



class EmployeeTimeSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeTimeSheet
        fields = '__all__'

        