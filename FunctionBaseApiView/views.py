from FunctionBaseApiView.serializers import StudentSerializer
from rest_framework .decorators import api_view
from rest_framework .response import Response
from rest_framework import status
from FunctionBaseApiView.models import Student
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def HomeView(request, pk=None):
    if request.method == 'GET':
        student = Student.objects.all()
        if student != '':
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
        serializer = StudentSerializer(student, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Update Successfully')
        return Response('Please Enter Valid Information')
    
    elif request.method == 'DELETE':
        pass