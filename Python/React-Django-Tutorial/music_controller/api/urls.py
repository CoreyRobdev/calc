from django.urls import path
from .views import RoomView

urlpatterns = [
  #if nothing is typed after the url run the 'main' function found in 'views.py'

  #'as_view()' gets the view for the class its ran on
    path('room', RoomView.as_view())
]