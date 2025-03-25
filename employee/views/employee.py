from django.shortcuts import render
from rest_framework import viewsets
from ..serializers import EmployeeCreateSerializer,EmployeeDocumentSerializer,EmployeeListSerializer,DocumentSerializer,EmployeeDetailSerializer,EmployeeProfileSerialier
from ..models import EmployeeDocument,Document,EmployeeProfile
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
from src.utils.response import error_response,success_response
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action



User = get_user_model()


class EmployeeViewSet(viewsets.ViewSet):
    # permission_classes = [IsStaff, IsAuthenticated]
    
    def list(self, request):
        """List all employees."""
        try:
            employees = CustomUser.objects.all()
            if not employees:
                return success_response([], "No employees found", status.HTTP_404_NOT_FOUND)
            
            serializer = EmployeeListSerializer(employees, many=True)
            return success_response(serializer.data, "Employee list retrieved")

        except Exception as e:
            return error_response("An error occurred while fetching employees", str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


    def create(self, request):
        """Create a new employee."""
        try:
            serializer = EmployeeCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return success_response(serializer.data, "Employee created successfully", status.HTTP_201_CREATED)

            return error_response("Failed to create employee", serializer.errors)

        
        except Exception as e:
            return error_response("An error occurred while creating employee", str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, pk=None):
        """Retrieve a specific employee."""
        try:
            employee = CustomUser.objects.filter(IID=pk).first()
            
            if not employee:
                return error_response(message="No Employee found",status_code=status.HTTP_404_NOT_FOUND,error="No Employee Found")
            serializer = EmployeeDetailSerializer(employee)


            return success_response(serializer.data, "Employee retrieved successfully")
        
        except Exception as e:
            print(e)
            return error_response("An error occurred while retrieving employee",str(e),status.HTTP_500_INTERNAL_SERVER_ERROR)


    @action(detail=True, methods=["post"])
    def change_status(self, request, pk=None):
        """Change the status of an employee."""
        try:
            employee = get_object_or_404(CustomUser, pk=pk)
            new_status = request.data.get("status")

            if employee.profile.status == new_status:
                return success_response(None,"No change in status required")
            
            employee.profile.status = new_status
            employee.profile.save()

            return success_response({"status": new_status},f"Status changed to {new_status}")
        
        except Exception as e:
            return Response({
                "data": None,
                "message": "Failed to change status",
                "status": "error",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=["get", "post"], url_name="profile", url_path="profile")
    def profile(self, request, pk=None):
        """Get or update employee profile."""
        try:
            profile = get_object_or_404(EmployeeProfile, user=pk)
            if request.method == "GET":
                serializer = EmployeeProfileSerialier(profile)
                return success_response(serializer.data,"Profile retrieved successfully")
                    
            elif request.method == "POST":
                print(request.data,request.method)
                serializer = EmployeeProfileSerialier(profile, data=request.data, partial=True)
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        "data": serializer.data,
                        "message": "Profile updated successfully",
                        "status": "success",
                        "error": None
                    }, status=status.HTTP_200_OK)
                
                return Response({
                    "data": None,
                    "message": "Failed to update profile",
                    "status": "error",
                    "error": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "data": None,
                "message": "An error occurred while handling profile",
                "status": "error",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





class EmployeeDocumentViewSet(viewsets.ModelViewSet):

    serializer_class = EmployeeDocumentSerializer
    queryset = EmployeeDocument.objects.all()






class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
