from rest_framework import serializers
from ValidatorApp.models import Student
from rest_framework .response import Response
from rest_framework import status

#1. Validator 
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name Should be start with r')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(validators = [start_with_r])
    roll_no = serializers.IntegerField()
    city = serializers.CharField()

    # create method
    def create(self, validated_data):
        print(validated_data)
        return Student.objects.create(**validated_data)
    
    #2. Field Level Validator
    # def validate_roll_no(self, value):
    #     if value >=200:
    #         raise serializers.ValidationError('Seat Full')
    #     return value

    #3. Object Level Validator
    # def validate(self, data):
    #     name = data.get('name')
    #     print('name :', name)
    #     city = data.get('city') 
    #     print('city :', city)
    #     print(type(city))
    #     if name == 'Manoj' and city == 'Jaipur':
    #         raise serializers.ValidationError('City Must Be Ranchi')
    #     return data

    
