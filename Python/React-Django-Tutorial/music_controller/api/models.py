from django.db import models
import string
import random

#Django allows us to write python code to be interpretted to a database table
#in Django you want to have FAT models and THIN views
#put most logic on models

def generate_unique_code():
  length = 6

  while True:
    #generates a random 'code' at 'k' length (here being 6) that only contains the uppercase ascii characters
    code = ''.join(random.choices(string.ascii_uppercase, k=length))
    #filters through all 'Room' objects by 'code' and checks if past codes are equal to the code generated here (this returns a list)
    #'.count()' counts the values in the list previously created (returns a number)
    if Room.objects.filter(code=code).count() == 0:
      break

    return code


# Create your models here.
class Room(models.Model):
  #every model has a 'primary key' (unique integer) that identifies the model created when the model is inserted into the database
  #define 'fields' aka pieces of info for each room
  #char field stores characters
  #'max_length' 'defualt' 'unique' are constraints to the field

  #'code' was created to identify the room
  #'host' stores info that links back to the host

  code = models.CharField(max_length=8, default="", unique=True)
  host = models.CharField(max_length=50, unique=True)
  guest_can_pause = models.BooleanField(null=False, default=False)
  votes_to_skip = models.IntegerField(null=False, default=1)
  #'auto_now_add' grabs the date and time the room is created at
  created_at = models.DateTimeField(auto_now_add=True)
