from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    specialization=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return f"Dr.{self.user.username} ({self.specialization})"
    

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    address=models.TextField()

    def __str__(self):
        return self.user.username
    


class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    reason=models.TextField()

    def __str__(self):
        return f"{self.patient.user.username} appointed to {self.doctor.user.username} on {self.date}"
