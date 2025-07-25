from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    """Serializer for the Listing model"""
    class Meta:
        model = Listing
        fields = [
            'id', 'host', 'title', 'description',
            'location', 'price_per_night', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    """Serializer for the Booking model"""
    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'guest', 'start_date',
            'end_date', 'status', 'status', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def validate(self, data):
        """Validate booking dates"""
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError(
                "End date must be after start date"
            )
        return data
