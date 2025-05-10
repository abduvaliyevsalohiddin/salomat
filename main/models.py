from django.db import models
from user.models import *


class CoreModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Order(CoreModel):
    doctor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='doctor_orders')
    patient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='patient_orders')
    consultation_date = models.DateTimeField()
    consultation_time = models.CharField(max_length=10, blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.doctor} && {self.patient} && {self.consultation_date}"


class Recommendations(CoreModel):
    doctor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='doctor_recommendations')
    patient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='patient_recommendations')
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.doctor} && {self.patient}"
