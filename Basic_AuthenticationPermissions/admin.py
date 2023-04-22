from django.contrib import admin
from Basic_AuthenticationPermissions.models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_no', 'city']