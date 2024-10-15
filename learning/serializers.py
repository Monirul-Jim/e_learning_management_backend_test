from rest_framework import serializers
from learning.models import CategoryModel


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'
