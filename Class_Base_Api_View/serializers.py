from rest_framework import serializers
from Class_Base_Api_View.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name', 'roll_no', 'city']