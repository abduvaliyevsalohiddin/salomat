from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ('patient', 'Patient'),
    ('doctor', 'Doctor'),
)


class Profile(AbstractUser):
    fathers_name = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')  # <== BU YERDA
    specialty = models.CharField(max_length=100, blank=True, null=True)
    experience = models.PositiveIntegerField(help_text="Years of experience", blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.username
#
#
# class Patient(models.Model):
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     blood_group = models.CharField(max_length=5)
#     weight = models.DecimalField(max_digits=5, decimal_places=2)
#     height = models.DecimalField(max_digits=5, decimal_places=2)
#
#     def __str__(self):
#         return f"Patient: {self.profile.phone}"
#
#
# class Doctor(models.Model):
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     specialty = models.CharField(max_length=100)
#     experience = models.PositiveIntegerField(help_text="Years of experience")
#     hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
#
#     def __str__(self):
#         return f"Doctor: {self.profile.phone} ({self.specialty})"
