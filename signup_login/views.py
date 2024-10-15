
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.utils import timezone


class RegistrationViewSet(viewsets.ViewSet):
    queryset = []
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data['user']
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            # Manually update last_login
            user.last_login = timezone.now()
            user.save()

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token

            # Create response with access token
            response = Response({
                'access': str(access_token),
            }, status=status.HTTP_200_OK)

            # Set refresh token in a cookie (HTTPOnly for security)
            cookie_max_age = 24 * 60 * 60  # 1 day
            response.set_cookie(
                key='refresh_token',
                value=str(refresh),
                httponly=True,  # Prevent JavaScript access
                secure=False,    # Ensure it's only sent over HTTPS
                samesite='Lax',  # Adjust SameSite attribute for CSRF protection
                max_age=cookie_max_age,  # Set max age for the cookie
            )

            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
