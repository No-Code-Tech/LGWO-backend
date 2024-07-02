from rest_framework import serializers
from ..models import Document,EmployeeDocument
import datetime


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = '__all__'




class EmployeeDocumentSerializer(serializers.HyperlinkedModelSerializer):

    is_valid = serializers.BooleanField(read_only=True)

    def to_internal_value(self, data):

        time = datetime.datetime.now()        
        issued_date = datetime.datetime.strptime(data['issued_date'],"%Y-%m-%d")
        expiry_date = datetime.datetime.strptime(data['expiry_date'],"%Y-%m-%d")

        if issued_date >= expiry_date:
            raise serializers.ValidationError({"error":"Expiry Date cannot be equal or smaller than Issued Date"})


        if expiry_date <= time:
            raise serializers.ValidationError({"error":"Expiry Date must be greater than current date"})


        # pprint(dict(data))
        return super().to_internal_value(data)
       



    class Meta:
        model = EmployeeDocument
        fields = '__all__'


