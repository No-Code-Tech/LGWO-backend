from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeDetailSerializer,BillSerializer,TimeSheetSerializer,EmployeeTimeSheetSerializer,DocumentSerializer,EmployeeDocumentSerializer,EmployeeListSerializer
from .models import EmployeeProfile,TimeSheet,Bill,Document,Country,EmployeeTimeSheet,EmployeeDocument
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from user.models import CustomUser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,authentication_classes,action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .permissions import GroupRequiredMixin
User = get_user_model()

class EmployeeViewSet(GroupRequiredMixin,viewsets.ModelViewSet):


    lookup_field = 'IID'
    # permission_classes = [IsOwner,IsAuthenticated]
    serializer_class = EmployeeDetailSerializer
    queryset = CustomUser.objects.filter(is_superuser =False)


    # def get_permission(self):
    #     if self.request.method == 'GET':
    #         print("It was here")
    #     return super().get_permission()


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

class EmployeeListView(GroupRequiredMixin,viewsets.ViewSet):
    group_name = 'employees'


    def list(self,request):
        user = CustomUser.objects.all()
        # serializer_data = EmployeeDetailSerializer(user,many=True,context={'request':request})
        serializer_data = EmployeeListSerializer(user,many=True)
        return Response({"data":serializer_data.data})

    # def get_permissions(self):
    #     if self.action=="get":
    #         permission_classes = [IsAuthenticated]
    #     else:
    #         permission_classes = []

    #     if self.action=="change_status":
    #         permission_classes = [IsAdminUser]


    #     return [permission() for permission in permission_classes]



    @action(detail=True,methods=["post"])   
    def change_status(self,request,pk=None):
        response = dict()

        user = get_object_or_404(User,pk=pk)
        status = request.data["status"]

        if user.profile.status == status:
            response["message"] = "No need to change status"

        else: 
            user.profile.status = status
            user.profile.save()
            response["message"] = f"Status is changed to {status}"
        


        return Response({"data":response})







