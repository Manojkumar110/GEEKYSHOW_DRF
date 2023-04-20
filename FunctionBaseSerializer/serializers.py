from rest_framework import serializers
from FunctionBaseSerializer.models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    roll_no = serializers.IntegerField()
    city = serializers.CharField()

    class Meta:
        model = Student
        fields = '__all__'
    
    def create(self, validated_data):
        print('validated_data', validated_data)
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name')
        instance.roll_no = validated_data.get('roll_no')
        instance.city = validated_data.get('city')
        instance.save()
        return instance