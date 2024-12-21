from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from learning.models import CategoryModel, CourseModel, ModuleModel, ParentModule, VideoModel, QuizModel
from learning.serializers import CategorySerializers, CourseSerializer, ModuleSerializer, ParentModuleSerializer, VideoSerializer, QuizSerializer
from django.http import JsonResponse
from learning.utils import send_response
from django.http import JsonResponse
from rest_framework.decorators import action


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


class ParentModuleViewSets(viewsets.ModelViewSet):
    queryset = ParentModule.objects.all()
    serializer_class = ParentModuleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return send_response(
            success=True,
            message="Parent Module created successfully",
            data=serializer.data,
            status_code=status.HTTP_201_CREATED
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return send_response(
            success=True,
            message="Parent Modules retrieved successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return send_response(
            success=True,
            message="Single Parent Module retrieved successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )


class ModuleViewSets(viewsets.ModelViewSet):
    queryset = ModuleModel.objects.all()
    serializer_class = ModuleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return send_response(
            success=True,
            message="Module created successfully",
            data=serializer.data,
            status_code=status.HTTP_201_CREATED
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return send_response(
            success=True,
            message="Modules retrieved successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return send_response(
            success=True,
            message="Single Module retrieved successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )


class VideoViewSets(viewsets.ModelViewSet):
    queryset = VideoModel.objects.all()
    serializer_class = VideoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return send_response(
            success=True,
            message="Video created successfully",
            data=serializer.data,
            status_code=status.HTTP_201_CREATED
        )

    @action(detail=False, methods=['get'], url_path='course/(?P<course_id>[^/.]+)')
    def list_course_videos(self, request, course_id=None):
        # Filter videos by course ID
        videos = self.queryset.filter(module__course__id=course_id)
        serializer = self.get_serializer(videos, many=True)
        return send_response(
            success=True,
            message="Videos retrieved successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return send_response(
            success=True,
            message="Single Video retrieved successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )


class QuizViewSets(viewsets.ModelViewSet):
    queryset = QuizModel.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        module_title = self.request.query_params.get(
            'module_title', None)  # Get 'module_title' query parameter
        if module_title:
            # Filter quizzes based on the module title (case insensitive)
            queryset = queryset.filter(module__title__iexact=module_title)
        return queryset

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return send_response(
            success=True,
            message="Quiz created successfully",
            data=serializer.data,
            status_code=status.HTTP_201_CREATED
        )

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return send_response(
            success=True,
            message="Quizzes retrieved successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return send_response(
            success=True,
            message="Single Quiz retrieved successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):

        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return send_response(
            success=True,
            message="Quiz updated successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        """
        Delete a quiz.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return send_response(
            success=True,
            message="Quiz deleted successfully",
            status_code=status.HTTP_204_NO_CONTENT
        )


def api_not_found(request, exception=None):
    return JsonResponse({
        'statusCode': 404,
        'success': False,
        'message': 'API Not Found!!',
        'error': ''
    }, status=404)
