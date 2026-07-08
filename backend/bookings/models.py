from django.db import models
from django.conf import settings
from hosting.models import Event


class Booking(models.Model):

    PAYMENT_STATUS = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed"),
        ("refunded", "Refunded"),
    ]

    BOOKING_STATUS = [
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings" )
    event = models.ForeignKey( Event, on_delete=models.CASCADE, related_name="bookings")

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    quantity = models.PositiveIntegerField(default=1)
    ticket_price = models.DecimalField( max_digits=10, decimal_places=2 )
    total_amount = models.DecimalField( max_digits=10, decimal_places=2)

    razorpay_order_id = models.CharField( max_length=200, unique=True)
    razorpay_payment_id = models.CharField( max_length=200, blank=True, null=True)
    razorpay_signature = models.CharField( max_length=500, blank=True, null=True)

    payment_status = models.CharField( max_length=20, choices=PAYMENT_STATUS, default="pending")
    booking_status = models.CharField( max_length=20, choices=BOOKING_STATUS, default="confirmed")

    booked_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-booked_at"]

    def __str__(self):
        return f"{self.user.name} - {self.event.event_name}"