from patient.models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patients
        fields=('id','firstname','lastname','age','dob','mobile','gender','comment','reg_date')