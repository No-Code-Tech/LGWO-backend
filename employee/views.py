from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeDetailSerializer,BillSerializer,TimeSheetSerializer,EmployeeTimeSheetSerializer,DocumentSerializer,EmployeeDocumentSerializer,EmployeeListSerializer
from .models import EmployeeProfile,TimeSheet,Bill,Document,Country,EmployeeTimeSheet,EmployeeDocument
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from user.models import CustomUser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,authentication_classes,action
from rest_framework.response import Response

class EmployeeViewSet(viewsets.ModelViewSet):

    lookup_field = 'id'
    # permission_classes = [IsOwner,IsAuthenticated]
    serializer_class = EmployeeListSerializer
    queryset = CustomUser.objects.all()


    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['request'] = self.request
    #     print(context)
    #     return context


class BillViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    serializer_class = BillSerializer
    queryset = Bill.objects.all()


class TimeSheetViewSet(viewsets.ModelViewSet):

    serializer_class = TimeSheetSerializer
    queryset = TimeSheet.objects.all()

class EmployeeTimeSheetViewSet(viewsets.ModelViewSet):


    serializer_class = EmployeeTimeSheetSerializer
    queryset = EmployeeTimeSheet.objects.all()


class DocumentViewSet(viewsets.ModelViewSet):

    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class EmployeeDocumentViewSet(viewsets.ModelViewSet):

    serializer_class = EmployeeDocumentSerializer
    queryset = EmployeeDocument.objects.all()

class EmployeeListView(viewsets.ViewSet):

    def list(self,request):
        user = CustomUser.objects.all()
        # serializer_data = EmployeeDetailSerializer(user,many=True,context={'request':request})
        serializer_data = EmployeeListSerializer(user,many=True)


        return Response({"data":serializer_data.data})

    def get_permissions(self):
        if self.action=="post":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []


        return [permission() for permission in permission_classes]


