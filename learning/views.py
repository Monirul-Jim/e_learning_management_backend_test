from rest_framework import viewsets
from learning.models import CategoryModel
from learning.serializers import CategorySerializers


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializers
