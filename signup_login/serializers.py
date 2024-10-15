
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'password1']

    def validate(self, data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError(
                {'password': 'Passwords do not match.'})
        return data

    def create(self, validated_data):
        validated_data.pop('password1')
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid email or password.')
        user = authenticate(username=user.username, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid email or password.')
        attrs['user'] = user
        return attrs
