from rest_framework import serializers
from learning.models import CategoryModel, CourseModel


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'