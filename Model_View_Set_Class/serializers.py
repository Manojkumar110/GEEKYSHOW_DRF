from rest_framework import serializers
from Model_View_Set_Class.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
