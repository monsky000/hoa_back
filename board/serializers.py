from rest_framework import serializers
from .models import *

class PositionsSerializers(serializers.ModelSerializer):
  class Meta:
    model=Positions
    fields='__all__'
    
class ElectionsSerializers(serializers.ModelSerializer):
  class Meta:
    model=Elections
    fields='__all__'
    
class NominationsSerializers(serializers.ModelSerializer):
  class Meta:
    model=Nominations
    fields='__all__'

class VotesSerializers(serializers.ModelSerializer):
  class Meta:
    model=Votes
    fields='__all__'