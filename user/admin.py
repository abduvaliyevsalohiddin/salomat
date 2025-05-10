from django.contrib import admin
from .models import *

admin.site.register(Profile)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import Profile, Patient, Doctor
#
#
# class PatientInline(admin.StackedInline):
#     model = Patient
#     can_delete = False
#     verbose_name_plural = 'Patient Info'
#     extra = 0
#
#
# class DoctorInline(admin.StackedInline):
#     model = Doctor
#     can_delete = False
#     verbose_name_plural = 'Doctor Info'
#     extra = 0
#
#
# @admin.register(Profile)
# class CustomProfileAdmin(UserAdmin):
#     model = Profile
#     list_display = ('username', 'email', 'phone', 'role', 'is_staff', 'is_active')
#     list_filter = ('role', 'is_staff', 'is_active')
#
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal Info', {'fields': ('email', 'fathers_name', 'phone', 'profile_picture')}),
#         ('Role Info', {'fields': ('role',)}),
#         ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'phone', 'role', 'password1', 'password2', 'is_staff', 'is_active'),
#         }),
#     )
#
#     search_fields = ('username', 'email', 'phone')
#     ordering = ('username',)
#
#     def get_inline_instances(self, request, obj=None):
#         """Dynamic inline based on user's role."""
#         inlines = []
#         if obj:
#             if obj.role == 'patient':
#                 inlines.append(PatientInline(self.model, self.admin_site))
#             elif obj.role == 'doctor':
#                 inlines.append(DoctorInline(self.model, self.admin_site))
#         return inlines
