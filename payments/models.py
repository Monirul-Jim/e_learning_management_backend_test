from django.db import models
from django.contrib.auth.models import User
from learning.models import CourseModel


class PurchaseOrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)

    # Optional fields
    stripe_session_id = models.CharField(
        max_length=255, blank=True, null=True)  # Track Stripe session
    # Optional to group purchases
    order_id = models.CharField(max_length=50, blank=True, null=True)
    payment_status = models.CharField(
        max_length=20, default='pending')  # Track payment status

    def __str__(self):
        return f'{self.user.email} purchased {self.course.title} for {self.total_amount}'
