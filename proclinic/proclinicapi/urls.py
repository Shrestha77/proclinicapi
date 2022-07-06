from django.urls import path
from proclinicapi import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('patient/', views.PatientView.as_view(), name='patient'),
    path('patientlist/', views.PatientView.as_view(), name='patientlist'),
    path('patient/<int:pk>/', views.PatientDetail.as_view(), name='patientdetail' ),
    path('patientvisit/', views.PatientVisitView.as_view(), name='patientvisit' ),
    path('doctor/', views.DoctorView.as_view(), name='doctor'),
    path('doctorlist/', views.DoctorView.as_view(), name='doctorlist'),
    path('doctor/<int:pk>/', views.DoctorDetail.as_view(), name='doctordetail' ),
    path('doctoractivity/', views.DoctorActivityView.as_view(), name='doctoractivity'),
]