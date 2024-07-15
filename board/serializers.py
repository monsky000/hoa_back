from rest_framework import serializers
from .models import *

class PositionsSerializers(serializers.ModelSerializer):
  class Meta:
    models=Positions
    fields='__all__'
    
class ElectionsSerializers(serializers.ModelSerializer):
  class Meta:
    models=Elections
    fields='__all__'
    
class NominationsSerializers(serializers.ModelSerializer):
  class Meta:
    models=Nominations
    fields='__all__'

class VotesSerializers(serializers.ModelSerializer):
  class Meta:
    models=Votes
    fields='__all__'