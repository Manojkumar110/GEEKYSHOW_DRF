from rest_framework import serializers
from SerializerApp.models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    roll_no = serializers.IntegerField()
    age = serializers.IntegerField()
    add = serializers.CharField()
 
    class Meta:
        model = Student
        fields = ('id',)
'''
Serializer Fields:-




'''

