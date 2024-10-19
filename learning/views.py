from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from learning.models import CategoryModel, CourseModel
from learning.serializers import CategorySerializers, CourseSerializer
from django.http import JsonResponse
from learning.utils import send_response
from django.http import JsonResponse


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return send_response(
            success=True,
            message="Category created successfully",
            data=serializer.data,
            status_code=status.HTTP_201_CREATED
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return send_response(
            success=True,
            message="Categories retrieved successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )


class CourseViewSets(viewsets.ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return send_response(
            success=True,
            message="Course created successfully",
            data=serializer.data,
            status_code=status.HTTP_201_CREATED
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return send_response(
            success=True,
            message="Courses retrieved successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return send_response(
            success=True,
            message="Single Course retrieved successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )


def api_not_found(request, exception=None):
    return JsonResponse({
        'statusCode': 404,
        'success': False,
        'message': 'API Not Found!!',
        'error': ''
    }, status=404)
