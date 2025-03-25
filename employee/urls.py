from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import EmployeeDocumentViewSet,EmployeeViewSet,EmployeeTimeSheetViewSet,BillViewSet,DocumentViewSet,attendance_rate
router = routers.SimpleRouter()
router.register(r'bills',BillViewSet)

router.register(r'document',DocumentViewSet)
router.register(r'employee-document',EmployeeDocumentViewSet)

urlpatterns = [

    path('attendance/<int:pk>',attendance_rate),


    path('employees',EmployeeViewSet.as_view(
        {
        'get':'list',
        'post':'create',
        }
        )),

    path('employee/<int:pk>/',EmployeeViewSet.as_view({
         'get':'retrieve',
         'post':'create',
    })),
    path('employee/profile/<int:pk>/',EmployeeViewSet.as_view({
        'get':'profile',
        'post':'profile'
    })
    ),
   
    path('change-status/<str:pk>/',EmployeeViewSet.as_view({'post':'change_status'})),

    
    path('timesheets',EmployeeTimeSheetViewSet.as_view({
        'get':'list',
        'post':'create'
    }))
    ]


timesheet_urls = [
    
]



urlpatterns += router.urls

