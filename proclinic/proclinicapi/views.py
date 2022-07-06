from django.http import Http404
from rest_framework.response import Response
from proclinicapi.models import Patient, Doctor, PatientVisits, DoctorActivity
from proclinicapi.serializers import PatientSerializer, DoctorSerializer, PatientVisitsSerializer, DoctorActivitySerializer, DoctorsAvailabilitySerializer
from rest_framework.views import APIView
from rest_framework import status


class PatientView(APIView):
    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully Done! Please add payment now', 'status': 'success', 'patient': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self, request, format=None):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response({'status': 'success', 'patient': serializer.data}, status=status.HTTP_200_OK)


class PatientDetail(APIView):
    # Retrieve, update or delete a patient instance.
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        patient = self.get_object(pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DoctorView(APIView):
    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully Done! Please Check in doctors list', 'status': 'success', 'doctor': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self, request, format=None):
        patients = Doctor.objects.all()
        serializer = DoctorSerializer(patients, many=True)
        return Response({'status': 'success', 'doctor': serializer.data}, status=status.HTTP_200_OK)


class DoctorDetail(APIView):
    # Retrieve, update or delete a doctor instance.
    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        doctor = self.get_object(pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PatientVisitView(APIView):
    def post(self, request, format=None):
        serializer = PatientVisitsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully Done! Please add payment now', 'status': 'success', 'patientvisit': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self, request, format=None):
        patientvisits = PatientVisits.objects.all()
        serializer = PatientVisitsSerializer(patientvisits, many=True)
        return Response({'status': 'success', 'patientvisit': serializer.data}, status=status.HTTP_200_OK)
    
class DoctorActivityView(APIView):
    def post(self, request, format=None):
        serializer = DoctorActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Successfully Done! Please add payment now', 'status': 'success', 'doctoractivity': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self, request, format=None):
        doctoractivity = DoctorActivity.objects.all()
        serializer = DoctorActivitySerializer(doctoractivity, many=True)
        return Response({'status': 'success', 'doctoractivity': serializer.data}, status=status.HTTP_200_OK)


class DashboardView(APIView):
    def get(self, request, format=None):
        totalpatient = len(Patient.objects.all())
        patient_year = Patient.objects.all().dates('last_visit', 'year')
        for years in patient_year:
           Patient.objects.filter(last_visit__year=years.year)
        doctorsavailability = Doctor.objects.all()
        serializer = DoctorsAvailabilitySerializer(doctorsavailability, many=True)
        return Response({'status': 'success', 'doctorsavailability': serializer.data, 'totalpatient': totalpatient, 'patient_year': patient_year}, status=status.HTTP_200_OK)
