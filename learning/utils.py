from django.http import JsonResponse
from rest_framework.response import Response


def api_not_found(request, exception=None):
    return JsonResponse({
        'statusCode': 404,
        'success': False,
        'message': 'API Not Found!!',
        'error': ''
    }, status=404)


def send_response(success, message, data=None, status_code=200):
    return Response({
        'statusCode': status_code,
        'success': success,
        'message': message,
        'data': data
    }, status=status_code)
