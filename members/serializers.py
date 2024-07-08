from rest_framework import serializers
from .models import MemReg, Occupants

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemReg
        fields = '__all__'