from rest_framework import serializers
from .models import MemReg, Occupants

class OccupantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupants
        fields = ['member', 'fullname', 'dob', 'relationship', 'gender']
    
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
        fields = [
            'reg_form_no', 'family_name', 'first_name', 'middle_name', 'blk', 'lot',
            'street', 'landline', 'mobile', 'email', 'fb_name', 'description',
            'profession', 'educ', 'occupants'
        ]

    def create(self, validated_data):
        occupants_data = validated_data.pop('occupants')
        memeber = MemReg.objects.create(**validated_data)
        for occupant_data in occupants_data:
            Occupants.objects.create(**occupant_data, memebers=memeber)
        return memeber

    def update(self, instance, validated_data):
        occupants_data = validated_data.pop('occupants')
        instance.reg_form_no = validated_data.get('reg_form_no', instance.reg_form_no)
        instance.family_name = validated_data.get('family_name', instance.family_name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.blk = validated_data.get('blk', instance.blk)
        instance.lot = validated_data.get('lot', instance.lot)
        instance.street = validated_data.get('street', instance.street)
        instance.landline = validated_data.get('landline', instance.landline)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.email = validated_data.get('email', instance.email)
        instance.fb_name = validated_data.get('fb_name', instance.fb_name)
        instance.description = validated_data.get('description', instance.description)
        instance.profession = validated_data.get('profession', instance.profession)
        instance.educ = validated_data.get('educ', instance.educ)
        instance.save()

        instance.occupants.all().delete()
        for occupant_data in occupants_data:
            Occupants.objects.create(**occupant_data, memebers=instance)
        
        return instance