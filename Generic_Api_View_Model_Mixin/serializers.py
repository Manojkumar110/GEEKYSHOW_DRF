from rest_framework import serializers
from Generic_Api_View_Model_Mixin.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'