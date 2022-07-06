from dataclasses import field
from rest_framework import serializers
from proclinicapi.models import Patient, Doctor, PatientVisits, DoctorActivity


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'date_of_birth', 'age', 'phone',
                  'email', 'gender', 'address', 'file']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'date_of_birth', 'specialization', 'experience', 'age', 'phone',
                  'email', 'gender', 'doctor_details', 'address', 'file']
        

class PatientVisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientVisits
        fields = [ 'patient','doctor', 'cost', 'visit_date', 'status']


class DoctorActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorActivity
        fields = ['doctor','patient', 'injury_condition', 'visit_date', 'status']


class DoctorsAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'availability']
