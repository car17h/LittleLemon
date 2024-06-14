from .models import Menu, Booking
from rest_framework import serializers

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
      model = Booking
      fields = ['id', 'name', 'no_of_guest', 'booking_date']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
      model = Menu
      fields = '__all__'