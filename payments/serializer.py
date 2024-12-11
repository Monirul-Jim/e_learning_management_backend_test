
from learning.models import CourseModel
from rest_framework import serializers
from payments.models import PurchaseOrderModel

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name',
                  'last_name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = ['id', 'title', 'description', 'image',
                  'price']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    course = CourseSerializer()

    class Meta:
        model = PurchaseOrderModel
        fields = ['id', 'total_amount', 'purchased_at', 'user', 'course',
                  'payment_status']
