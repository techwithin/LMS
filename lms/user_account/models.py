from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dept=models.CharField(max_length=11, blank=False)
    year=models.CharField(max_length=11, blank=False)
    phone_number = models.CharField(max_length=11, blank=False)
    registration_no=models.CharField(max_length=11, blank=False)

    address = models.CharField(max_length=50, default="")
    unique_Id = models.CharField(max_length=11, blank=False)

    def __str__(self):
        return str(self.user)



class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dept=models.CharField(max_length=11, blank=False)
    subject=models.CharField(max_length=11, blank=False)
    phone_number = models.CharField(max_length=11, blank=False)
    joining=models.CharField(max_length=11, blank=False)

    address = models.CharField(max_length=50, default="")
    #unique_Id = models.CharField(max_length=11, blank=False)

    def __str__(self):
        return str(self.user)

class ID(models.Model):
   unique_Id = models.CharField(max_length=100)