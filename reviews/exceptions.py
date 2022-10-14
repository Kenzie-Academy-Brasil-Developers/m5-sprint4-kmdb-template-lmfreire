from rest_framework.exceptions import APIException
from rest_framework.views import status

class ValidationKeyError(APIException):
    status_code = status.HTTP_403_FORBIDDEN