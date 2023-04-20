from rest_framework.decorators import api_view
from rest_framework.response import Response
from ModelSerializer.serializers import StudentSerializer
from ModelSerializer.models import Student
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST', 'PUT','DELETE'])
def HomeView(request, pk=None):
    if request.method == 'GET':
        student = Student.objects.all()
        if student:
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        student = Student.objects.get(pk=pk)
        print(student)
        serializer = StudentSerializer(student, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

    # elif request.method == 'DELETE':
    #     print('PK :',pk)
    #     student = Student.objects.filter(roll_no=1)
    #     print('student :',student)
    #     student.delete()
    #     return Response('Data Delete')

