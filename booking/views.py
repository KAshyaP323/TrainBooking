from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from booking.serializers import Train_serializer,Passenger_serializer
from booking.models import TrainDB,PassengerDB

class TrainListCreateView(APIView):
    def get(self,request):
        qs=TrainDB.objects.all()
        serializer_instance=Train_serializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=Train_serializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class TrainRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs=get_object_or_404(TrainDB,id=pk)
        serializer_instance=Train_serializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        form_data=request.data
        train_object=get_object_or_404(TrainDB,id=pk)
        serializer_instance=Train_serializer(data=form_data,instance=train_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        train_object=get_object_or_404(TrainDB,id=pk)
        train_object.delete()
        return Response(data={"Message":"Deleted.."})

class PassengerListCreateView(APIView):
    def get(self,request):
        qs=PassengerDB.objects.all()
        serializer_instance=Passenger_serializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=Passenger_serializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class PassengerRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs=get_object_or_404(PassengerDB,id=pk)
        serializer_instance=Passenger_serializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        form_data=request.data
        passenger_object=get_object_or_404(PassengerDB,id=pk)
        serializer_instance=Passenger_serializer(data=form_data,instance=passenger_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        passenger_object=get_object_or_404(PassengerDB,id=pk)
        passenger_object.delete()
        return Response(data={"Message":"Deleted.."})