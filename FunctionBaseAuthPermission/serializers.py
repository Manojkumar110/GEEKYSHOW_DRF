from rest_framework import serializers
from FunctionBaseAuthPermission.models import Student1, Student2

class StudentSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Student1
        fields = '__all__'

class StudentSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Student2
        fields = '__all__'