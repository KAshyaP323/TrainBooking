from django.db import models

# Create your models here.
class TrainDB(models.Model):
    train_name=models.CharField(max_length=200)
    train_number=models.PositiveIntegerField()
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    departure_time=models.TimeField()
    arrival_time=models.TimeField()
    available_seats=models.PositiveIntegerField()

    def __str__(self):
        return self.train_name

class PassengerDB(models.Model):
    passenger_name=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    train_id=models.IntegerField()
    journey_date=models.DateField()
    seat_number=models.PositiveIntegerField()
    status=models.CharField(max_length=100,default="Confirmed")

    def __str__(self):
        return self.passenger_name