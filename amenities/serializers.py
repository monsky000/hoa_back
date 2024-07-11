from rest_framework import serializers
from .models import *

class AmenitiesSerializers(serializers.ModelSerializer):
  class Meta:
    model = Amenities
    fields = '__all__'

class ReservationsSerializers(serializers.ModelSerializer):
  class Meta:
    model = Reservations
    fields = '__all__'
        
class MaintenanceSerializers(serializers.ModelSerializer):
  class Meta:
    model = Maintenance
    fields = '__all__'