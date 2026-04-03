# hello/exceptions.py
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    """
    DRF default exception_handler шақырылады,
    кейін біз өзіміздің форматты қосамыз.
    """
    response = exception_handler(exc, context)

    if response is not None:
        customized_response = {
            "success": False,
            "error": {
                "status_code": response.status_code,
                "message": response.data
            }
        }
        return Response(customized_response, status=response.status_code)

    # Егер response None болса, default 500
    return Response({
        "success": False,
        "error": {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": str(exc)
        }
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)