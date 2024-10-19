from django.db import models


class Order(models.Model):
    customer_email = models.EmailField(default='a@gmail.com')
    # Assuming you want to keep this field
    customer_name = models.CharField(max_length=255, default='a')
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    payment_intent = models.CharField(max_length=255, blank=True, null=True)
    course_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.customer_email} - ${self.total_amount:.2f}"
