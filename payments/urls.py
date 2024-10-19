from django.urls import path
from .views import StripeCheckoutView, OrderCourseView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'orders', OrderCourseView, basename='order')
urlpatterns = [
    path('create-checkout-session/', StripeCheckoutView.as_view()),
    path('', include(router.urls)),
]
