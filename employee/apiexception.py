from rest_framework.exceptions import APIException

class NoPermissionToPerfom(APIException):
    status = 403
    default_detail = "You are not permitted to perform this action/task"
    default_code = "forbidden"