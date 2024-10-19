
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
import stripe
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeCheckoutView(APIView):
    def post(self, request):
        try:
            total_amount = request.data.get('totalAmount', 0)

            total_amount_cents = int(float(total_amount) * 100)
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

            return Response({'url': checkout_session.url}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
