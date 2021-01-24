from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.

#'APIView' lets us view a list of all 'Rooms'
#'APIView' takes a 'queryset' and 'serializer class'
#'queryset' is the list being viewed
#'serializer_class' gives us a way to view the list

#creates a view that returns all 'Room' objects
class RoomView(generics.ListAPIView):
  queryset = Room.objects.all()
  serializer_class = RoomSerializer
