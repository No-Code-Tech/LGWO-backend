from rest_framework import serializers
from ..models import TimeSheet



class TimeSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeSheet
        fields = '__all__'