from rest_framework import serializers
from ..models import Position,EmployeePosition



class PositionSerializer(serializers.Serializer):


    class Meta:
        model = Position
        fields = '__all__'


class EmployeePositionSerializer(serializers.Serializer):


    class Meta:
        model = EmployeePosition
        fields = '__all__'