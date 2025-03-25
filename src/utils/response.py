from rest_framework import status
from rest_framework.response import Response



def success_response(data,message="Success",status_code=status.HTTP_200_OK):
    return Response(
        {
            "data":data,
            "message":message,
            "status":"success",
            "error":None
        },status=status_code
    )

def error_response(message="Error",error=None,status_code=status.HTTP_400_BAD_REQUEST):
    return Response({
            "data": [],
            "message": message,
            "status": "error",
            "error": error
        }, status=status_code)