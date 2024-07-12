from rest_framework import serializers
from .models import MemReg, Occupants

class OccupantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupants
        fields = ['givenname','surname','age','relationship','gender']
    
class MembersSerializer(serializers.ModelSerializer):
    occupants = serializers.SerializerMethodField()
    class Meta:
        model = MemReg
        fields = '__all__'

    def get_occupants(self, obj):
        occupants = Occupants.objects.filter(member=obj)
        return OccupantsSerializer(occupants, many=True).data

class AddMemberSerializer(serializers.ModelSerializer):
    occupants = OccupantsSerializer(many=True)
    class Meta:
        model = MemReg
        fields = ['reg_form_no','family_name','first_name','middle_name','blk','lot','street','landline','mobile','email','fb_name','description','reg_status','educ','profession','is_deleted','occupants'
]

    def create(self, validated_data):
        occupants_data = validated_data.pop('member', [])
        member = MemReg.objects.create(**validated_data)
        for occupant_data in occupants_data:
            occupant_data['occupants'] = member
            Occupants.objects.create(**occupants_data)
        return member