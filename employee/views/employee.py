from django.shortcuts import render
from rest_framework import viewsets
from ..serializers import EmployeeCreateSerializer,EmployeeDocumentSerializer,EmployeeListSerializer,DocumentSerializer,EmployeeDetailSerializer
from ..models import EmployeeDocument,Document
from ..permissions import IsOwner
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from user.models import CustomUser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,authentication_classes,action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from ..permissions import GroupRequiredMixin,IsStaff
from rest_framework import status
User = get_user_model()

class EmployeeViewSet(viewsets.ViewSet):
    # permission_classes = [IsStaff,IsAuthenticated]
    def list(self,request):
        try:
            message = "All employees List"
            error=None
            user = CustomUser.objects.all()

            if not user:
                message = "No employee"
            serializer_data = EmployeeListSerializer(user,many=True)
            status = "success"
            status_code = None

        except Exception as e:
                return Response({
                    "data": None,
                    "message": "Failed to create user",
                    "status": "error",
                    "error": str(e)
                }, status=status.HTTP_400_BAD_REQUEST)

        return Response({"data":serializer_data.data,
                        "message":message,
                        "status":"success",
                        "error":error
                        })


    def create(self, request):
        try:
            serializer = EmployeeCreateSerializer(data=request.data)
            if serializer.is_valid():
                

                serializer.save()
                print("It was here")
                return Response({
                    "data": serializer.data,  
                    "message": "User has been successfully created",
                    "status": "success",
                    "error": None
                })
            else:
                return Response({
                    "data": None,
                    "message": "Failed to create user",
                    "status": "error",
                    "error": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "data": None,
                "message": "An error occurred",
                "status": "error",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self,request,pk):
        try:
            user = get_object_or_404(User,pk=pk)
            data = EmployeeDetailSerializer(user).data
            
            return Response({
                "data":data,
                "message":"User info has been retrieved successfully",
                "status":"success",
                "error":None
            })


        except Exception as e:
            return Response({
                "data": None,
                "message": "An error occurred",
                "status": "error",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







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








class EmployeeDocumentViewSet(viewsets.ModelViewSet):

    serializer_class = EmployeeDocumentSerializer
    queryset = EmployeeDocument.objects.all()






class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
