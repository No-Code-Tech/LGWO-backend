from django.shortcuts import render
from rest_framework import viewsets
from ..serializers import EmployeeDetailSerializer,BillSerializer,TimeSheetSerializer,EmployeeTimeSheetSerializer,DocumentSerializer,EmployeeDocumentSerializer,EmployeeListSerializer
from ..models import EmployeeProfile,TimeSheet,Bill,Document,Country,EmployeeTimeSheet,EmployeeDocument
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
User = get_user_model()


class TimeSheetViewSet(viewsets.ModelViewSet):

    serializer_class = TimeSheetSerializer
    queryset = TimeSheet.objects.all()

class EmployeeTimeSheetViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeTimeSheetSerializer
    queryset = EmployeeTimeSheet.objects.all()




class BillViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    serializer_class = BillSerializer
    queryset = Bill.objects.all()
