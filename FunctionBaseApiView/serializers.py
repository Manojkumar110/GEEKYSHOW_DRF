from rest_framework import serializers
from FunctionBaseApiView.models import Student

class StudentSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(write_only = True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll_no', 'city']