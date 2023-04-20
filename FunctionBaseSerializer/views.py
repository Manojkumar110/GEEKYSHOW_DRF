from rest_framework.response import Response
from rest_framework.decorators import api_view
from FunctionBaseSerializer.serializers import StudentSerializer
from rest_framework import status
from FunctionBaseSerializer.models import Student
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def HomeView(request, pk=None):
    if request.method == 'GET':
        if pk==None:
            students = Student.objects.all()
            print('students object', students)
            serializer = StudentSerializer(students, many=True)
            print('serializer',serializer)
            print('serializer data :',serializer.data)
            return Response(serializer.data)
        else:
            students = Student.objects.get(pk=pk)
            serializer = StudentSerializer(students)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        print('serializer', serializer)
        if serializer.is_valid():
            serializer.save()
            print('serializer data', serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        print('PK :',pk)
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_426_UPGRADE_REQUIRED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        stu = Student.objects.get(pk=pk) 
        stu.delete()