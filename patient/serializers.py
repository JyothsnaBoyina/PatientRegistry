from patient.models import *
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patients
        fields=('id','firstname','lastname','age','dob','mobile','gender','comment','reg_date')