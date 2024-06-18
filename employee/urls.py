from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import EmployeeViewSet,TimeSheetViewSet,BillViewSet,EmployeeTimeSheetViewSet,DocumentViewSet,EmployeeDocumentViewSet,EmployeeListView

router = routers.SimpleRouter()
router.register(r'employees',EmployeeViewSet)
router.register(r'timesheet',TimeSheetViewSet)
router.register(r'bills',BillViewSet)
router.register(r'employee-timesheet',EmployeeTimeSheetViewSet)
router.register(r'document',DocumentViewSet)
router.register(r'employee-document',EmployeeDocumentViewSet)

urlpatterns = [
    path('employee-detail',EmployeeListView.as_view({'get':'list'}))
    ]


urlpatterns += router.urls
