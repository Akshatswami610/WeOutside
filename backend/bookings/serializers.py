from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"

        read_only_fields = (
            "user",
            "payment_status",
            "booking_status",
            "booked_at",
            "updated_at",
            "razorpay_order_id",
            "razorpay_payment_id",
            "razorpay_signature",
        )