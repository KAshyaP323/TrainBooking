from rest_framework import serializers
from booking.models import TrainDB,PassengerDB

class Train_serializer(serializers.ModelSerializer):
    class Meta:
        model=TrainDB
        fields="__all__"
        read_only_fields=["id"]

class Passenger_serializer(serializers.ModelSerializer):
    class Meta:
        model=PassengerDB
        fields="__all__"
        read_only_fields=["id"]