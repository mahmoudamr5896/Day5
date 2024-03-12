from rest_framework import serializers
from company.models import Epmloyee ,TeamLeader

class EmployeeSerilazer(serializers.ModelSerializer):

    class Meta:
        model= Epmloyee
        fields= '__all__'

class TeamSerializer(serializers.ModelSerializer):

    manager=EmployeeSerilazer()
    class Meta:
        model=TeamLeader
        fields="__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    
    team=TeamSerializer()

    class Meta:
        model=Epmloyee
        fields="__all__"

