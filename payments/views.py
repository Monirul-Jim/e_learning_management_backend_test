
from .models import PurchaseOrderModel
from payments.models import PurchaseOrderModel
from learning.models import CourseModel
from django.contrib.auth.models import User
from rest_framework.views import APIView
import stripe
from django.conf import settings
from rest_framework.response import Response
from rest_framework import viewsets, status
from payments.serializer import PurchaseOrderSerializer
stripe.api_key = settings.STRIPE_SECRET_KEY

# class StripeCheckoutView(APIView):
#     def post(self, request):
#         try:
#             total_amount = request.data.get('totalAmount', 0)

#             total_amount_cents = int(float(total_amount) * 100)
#             checkout_session = stripe.checkout.Session.create(
#                 payment_method_types=['card'],
#                 line_items=[{
#                     'price_data': {
#                         'currency': 'usd',
#                         'product_data': {
#                             'name': 'Total Order Amount',
#                         },
#                         'unit_amount': total_amount_cents,
#                     },
#                     'quantity': 1,
#                 }],
#                 mode='payment',
#                 success_url=settings.SITE_URL +
#                 '?success=true&session_id={CHECKOUT_SESSION_ID}',
#                 cancel_url=settings.SITE_URL + '?canceled=true',
#             )

#             return Response({'url': checkout_session.url}, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StripeCheckoutView(APIView):
    def post(self, request):
        try:
            user_data = request.data.get('userData', {})
            courses = request.data.get('courses', [])
            total_amount = request.data.get('totalAmount', 0)

            # Ensure that userData and courses are not empty
            if not user_data or not courses:
                return Response({'error': 'User data or courses missing'}, status=status.HTTP_400_BAD_REQUEST)

            # Fetch or create the user
            user, created = User.objects.get_or_create(
                email=user_data['email'],
                defaults={
                    'first_name': user_data['first_name'], 'last_name': user_data['last_name']}
            )

            total_amount_cents = int(float(total_amount) * 100)

            # Create a checkout session with Stripe
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Total Order Amount',
                        },
                        'unit_amount': total_amount_cents,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=settings.SITE_URL +
                '?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=settings.SITE_URL + '?canceled=true',
            )

            # Create purchase order entries in the database for each course
            for course_data in courses:
                course = CourseModel.objects.get(id=course_data['id'])
                PurchaseOrderModel.objects.create(
                    user=user,
                    course=course,
                    # Store individual course price
                    total_amount=course_data['price']
                )

            return Response({'url': checkout_session.url}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class OrderCourseView(viewsets.ModelViewSet):
#     queryset = PurchaseOrderModel.objects.all()
#     serializer_class = PurchaseOrderSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, *args, **kwargs):
#         """Override retrieve method to add custom behavior if needed."""
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

#     def list(self, request, *args, **kwargs):
#         """Override list method if custom behavior is needed; otherwise, the default is fine."""
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


class OrderCourseView(viewsets.ModelViewSet):
    queryset = PurchaseOrderModel.objects.all()
    serializer_class = PurchaseOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """Override retrieve method to add custom behavior if needed."""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        """Filter orders by user email if provided."""
        email = request.query_params.get('email', None)
        queryset = self.get_queryset()

        if email:
            queryset = queryset.filter(
                user__email=email)  # Filter by user email

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
