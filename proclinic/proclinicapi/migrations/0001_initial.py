# Generated by Django 4.0.6 on 2022-07-06 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('specialization', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=200, null=True)),
                ('age', models.PositiveIntegerField(null=True)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=100)),
                ('doctor_details', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/patientfile/')),
                ('availability', models.CharField(choices=[('Available', 'Available'), ('On Leave', '\tOn Leave'), ('Not Available', '\tNot Available')], max_length=50)),
            ],
            options={
                'db_table': 'proclinicapi_doctor',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('age', models.PositiveIntegerField(null=True)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/patientfile/')),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Cancelled', '\tCancelled')], max_length=50)),
                ('last_visit', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'proclinicapi_patient',
            },
        ),
        migrations.CreateModel(
            name='PatientVisits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.PositiveIntegerField(null=True)),
                ('visit_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='proclinicapi.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='proclinicapi.patient')),
            ],
            options={
                'db_table': 'proclinicapi_patientvisits',
            },
        ),
        migrations.CreateModel(
            name='DoctorActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('injury_condition', models.CharField(max_length=200)),
                ('visit_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docotor', to='proclinicapi.doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='proclinicapi.patient')),
            ],
            options={
                'db_table': 'proclinicapi_doctoractivity',
            },
        ),
    ]
