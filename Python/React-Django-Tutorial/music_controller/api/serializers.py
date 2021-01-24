from rest_framework import serializers
from .models import Room
#takes a 'model' and translate it to a 'json' response

class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')

