from rest_framework.decorators import api_view
from rest_framework.response import Response
from ValidatorApp.models import Student
from rest_framework import status
from ValidatorApp.serializers import StudentSerializer
# Create your views here.

''''
------------Validation------------------
1.Field Level Validation
2.Object Level Validation
3.Validator

'''
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def HomeView(request):
    if request.method == 'GET':
        student = Student.objects.all()
        if student:
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)