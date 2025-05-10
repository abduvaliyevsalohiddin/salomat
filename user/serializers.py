from rest_framework import serializers
from .models import *


# Umumiy Profile uchun serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        return Profile.objects.create_user(**validated_data)

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = Profile
#         fields = '__all__'
#
#     def create(self, validated_data):
#         role = validated_data.get('role')
#         password = validated_data.pop('password')
#
#         # create_user orqali foydalanuvchi yaratish
#         profile = Profile.objects.create_user(password=password, **validated_data)
#
#         # Role asosida Doctor yoki Patient obyektini yaratish
#         if role == 'doctor':
#             Doctor.objects.create(profile=profile)
#         elif role == 'patient':
#             Patient.objects.create(profile=profile)
#
#         return profile
#
#
# # Umumiy Profile uchun serializer
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'
#
#
# # Bemor
# class PatientDetailSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer()
#
#     class Meta:
#         model = Patient
#         fields = '__all__'
#
#     def update(self, instance, validated_data):
#         profile_data = validated_data.pop('profile', {})
#         profile = instance.profile
#
#         # Profileni yangilash
#         for attr, value in profile_data.items():
#             setattr(profile, attr, value)
#         profile.save()
#
#         # Patientni yangilash
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         instance.save()
#
#         return instance
#
#
# # Doktor
# class DoctorDetailSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer()
#
#     class Meta:
#         model = Doctor
#         fields = '__all__'
#
#     def update(self, instance, validated_data):
#         profile_data = validated_data.pop('profile', {})
#         profile = instance.profile
#
#         # Profileni yangilash
#         for attr, value in profile_data.items():
#             setattr(profile, attr, value)
#         profile.save()
#
#         # Doctorni yangilash
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         instance.save()
#
#         return instance
