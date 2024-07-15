from rest_framework import serializers
from .models import *

class AmenitiesSerializers(serializers.ModelSerializer):
  class Meta:
    model = Amenities
    fields = '__all__'

class ReservationsSerializers(serializers.ModelSerializer):
  first_name = serializers.CharField(source='member.first_name', read_only=True)
  family_name = serializers.CharField(source='member.family_name', read_only=True)
  amenity_name = serializers.CharField(source='amenity.amenity_name', read_only=True)
  class Meta:
    model = Reservations
    fields = '__all__'
        
class MaintenanceSerializers(serializers.ModelSerializer):
  amenity_name = serializers.CharField(source='amenity.amenity_name', read_only=True)
  contractor_name = serializers.CharField(source='contractor.contractor_name', read_only=True)
  class Meta:
    model = Maintenance
    fields = '__all__'