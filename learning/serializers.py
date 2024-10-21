from rest_framework import serializers
from learning.models import CategoryModel, CourseModel, ModuleModel, ParentModule, VideoModel


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


class ModuleSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(
        queryset=CourseModel.objects.all())
    parent_module = serializers.PrimaryKeyRelatedField(
        queryset=ParentModule.objects.all())

    class Meta:
        model = ModuleModel
        fields = ['id', 'course', 'title',
                  'parent_module', 'description']


class VideoSerializer(serializers.ModelSerializer):
    # module = ModuleSerializer(read_only=True)
    module = serializers.PrimaryKeyRelatedField(
        queryset=ModuleModel.objects.all())

    class Meta:
        model = VideoModel
        fields = ['id', 'module', 'title', 'video_url', 'duration']
