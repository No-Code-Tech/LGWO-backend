from django.shortcuts import render
from rest_framework import viewsets
from ..serializers import EmployeeDetailSerializer,BillSerializer,EmployeeTimeSheetSerializer,DocumentSerializer,EmployeeDocumentSerializer,EmployeeListSerializer
from ..models import EmployeeProfile,Bill,Document,Country,EmployeeTimeSheet,EmployeeDocument
from ..permissions import IsOwner
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from user.models import CustomUser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,authentication_classes,action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from ..permissions import GroupRequiredMixin
from src.utils.response import success_response,error_response
from rest_framework.decorators import api_view
from rest_framework import status

User = get_user_model()


class EmployeeTimeSheetViewSet(viewsets.ViewSet):
    
    def list(self,request,pk=None):
        if pk:
            return success_response(None,"success")
        else:
            return success_response(None,"success")

    def create(self,request):
        pass

    def retrieve(self,request):
        pass
    
    



class BillViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    serializer_class = BillSerializer
    queryset = Bill.objects.all()


'''
function that returns recent year attendance rate with category
'''
@api_view(['get'])
def attendance_rate(request,pk):
    total_time_sheet = EmployeeTimeSheet.objects.filter(employee=pk)
    
    response = {}

    if not total_time_sheet:
        return error_response("No Timesheet Found","Error", status.HTTP_404_NOT_FOUND)



    for i in total_time_sheet:
        date_time = i.duty_start_time.strftime("%Y-%m")
    
        if date_time not in response:

            if i.duty_status:
                
                response[date_time] = {
                    "ABSENT":0,
                    "SICK":0,
                    "LEAVE":0,
                    "PRESENT":0
                }

                response[date_time][i.duty_status] += 1
        else:
            if i.duty_status:
                response[date_time][i.duty_status] += 1

        res = []
        if response:
            for i in response:
                res.append({
                    "name":i,
                    **response[i]
                })

            

            return success_response(data=res)

        
            





