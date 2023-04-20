from rest_framework import serializers
from ModelSerializer.models import Student


#1. Validator 
# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError('Name Should be start with r')


class StudentSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Student
        fields = ['id','name', 'roll_no', 'city']
        # fields = '__all__'
        # exclude = 'roll_no'
        # read_only = ['fields Name']
        # extra_kwrgs = {'name':{'read_only':True}}

# Serializer Validatiom :-
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
