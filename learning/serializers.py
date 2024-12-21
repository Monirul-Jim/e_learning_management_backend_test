from rest_framework import serializers
from learning.models import CategoryModel, CourseModel, ModuleModel, ParentModule, VideoModel, QuizModel


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'category', 'slug']


# class CourseSerializer(serializers.ModelSerializer):
#     categories = CategorySerializers(many=True)
#     # categories = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = CourseModel
#         fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=CategoryModel.objects.all()
    )
    category_details = CategorySerializers(
        many=True, read_only=True, source='categories')

    class Meta:
        model = CourseModel
        fields = ['id', 'image', 'title', 'description',
                  'price', 'categories', 'category_details']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('categories')
        return representation


class ParentModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentModule
        fields = ['id', 'title']


# class ModuleSerializer(serializers.ModelSerializer):
#     # course = serializers.PrimaryKeyRelatedField(
#     #     queryset=CourseModel.objects.all())
#     # parent_module = serializers.PrimaryKeyRelatedField(
#     #     queryset=ParentModule.objects.all())
#     course = CourseSerializer()
#     parent_module = ParentModuleSerializer()

#     class Meta:
#         model = ModuleModel
#         fields = ['id', 'course', 'title',
#                   'parent_module', 'description']
# class ModuleSerializer(serializers.ModelSerializer):
#     course = serializers.PrimaryKeyRelatedField(
#         queryset=CourseModel.objects.all()
#     )
#     parent_module = serializers.PrimaryKeyRelatedField(
#         queryset=ParentModule.objects.all(), required=False
#     )

#     class Meta:
#         model = ModuleModel
#         fields = ['id', 'course', 'title', 'parent_module', 'description']
class ModuleSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(
        queryset=CourseModel.objects.all(), write_only=True)
    course_details = CourseSerializer(read_only=True, source='course')
    parent_module = serializers.PrimaryKeyRelatedField(
        queryset=ParentModule.objects.all(), required=False, write_only=True)
    parent_module_details = ParentModuleSerializer(
        read_only=True, source='parent_module')

    class Meta:
        model = ModuleModel
        fields = ['id', 'course', 'course_details', 'title',
                  'parent_module', 'parent_module_details', 'description']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('course', None)
        representation.pop('parent_module', None)
        return representation


# class VideoSerializer(serializers.ModelSerializer):
#     module = ModuleSerializer()

#     # module = serializers.PrimaryKeyRelatedField(
#     #     queryset=ModuleModel.objects.all())

#     class Meta:
#         model = VideoModel
#         fields = ['id', 'module', 'title',
#                   'video_url', 'duration']


class VideoSerializer(serializers.ModelSerializer):
    module = serializers.PrimaryKeyRelatedField(
        queryset=ModuleModel.objects.all(), write_only=True
    )  # Write-only field to accept module ID
    module_details = ModuleSerializer(
        source='module', read_only=True)  # Read-only nested field

    class Meta:
        model = VideoModel
        fields = ['id', 'title', 'video_url',
                  'duration', 'module', 'module_details']


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizModel
        fields = ['id', 'module', 'title', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions', None)

        if not isinstance(questions_data, dict):
            raise serializers.ValidationError(
                {"questions": "Questions should be a dictionary."})

        quiz = QuizModel.objects.create(
            **validated_data,
            questions=questions_data
        )
        return quiz

    def update(self, instance, validated_data):
        questions_data = validated_data.pop('questions', None)

        if questions_data:
            instance.questions = questions_data

        # Update other fields
        instance.module = validated_data.get('module', instance.module)
        instance.title = validated_data.get('title', instance.title)
        instance.save()

        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['questions'] = instance.questions
        return representation
