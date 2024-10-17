from rest_framework import serializers
from learning.models import CategoryModel, CourseModel


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'category']


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
