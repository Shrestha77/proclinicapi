from django.contrib import admin
from proclinicapi.models import Patient, Doctor, PatientVisits, DoctorActivity
# Register your models here.

@admin.register(Patient)
class PatientModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','date_of_birth', 'age', 'phone', 'email', 'gender', 'address', 'file', 'last_visit', 'status']
    
@admin.register(Doctor)
class DoctorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_of_birth', 'specialization', 'experience', 'age', 'phone',
                    'email', 'gender', 'doctor_details', 'address', 'file', 'availability']
    

@admin.register(PatientVisits)
class PatientVisitsModelAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'cost', 'visit_date', 'status']
    

@admin.register(DoctorActivity)
class DoctorActivityModelAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient',
                    'injury_condition', 'visit_date', 'status']
