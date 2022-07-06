from django.db import models

# Create your models here.
STATUS_CHOICE = ((
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Cancelled', '	Cancelled'),
))
class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    age = models.PositiveIntegerField(null=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/patientfile/', null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=50)
    last_visit = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'proclinicapi_patient'
        
    
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    specialization = models.CharField(max_length=200)
    experience = models.CharField(max_length=200, null=True)
    age = models.PositiveIntegerField(null=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=100)
    doctor_details = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/patientfile/', null=True, blank=True)
    availability = models.CharField(
        choices=[('Available', 'Available'), ('On Leave', '	On Leave'), ('Not Available', '	Not Available')], max_length=50)
    
    def __str__(self):
            return self.name
    
    class Meta:
        db_table = 'proclinicapi_doctor'
        
        
class PatientVisits(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL, null=True)
    cost = models.PositiveIntegerField(null=True) # when payment model is created it should be change 
    visit_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100)
       
    def __str__(self):
            return self.status
    
    class Meta:
        db_table = 'proclinicapi_patientvisits'
    
class DoctorActivity(models.Model):
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='docotor')
    patient = models.ForeignKey(
        Patient, on_delete=models.SET_NULL, null=True)
    injury_condition = models.CharField(max_length=200)
    visit_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100)
    
    def __str__(self):
            return self.status
    
    class Meta:
        db_table = 'proclinicapi_doctoractivity'