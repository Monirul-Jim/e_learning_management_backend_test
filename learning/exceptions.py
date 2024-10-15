from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            'statusCode': response.status_code,
            'success': False,
            'message': response.data.get('detail', 'An error occurred'),
            'error': response.data
        }
    else:
        response = Response({
            'statusCode': 500,
            'success': False,
            'message': 'Something went wrong',
            'error': str(exc)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
