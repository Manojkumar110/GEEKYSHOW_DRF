from rest_framework.decorators import api_view
from rest_framework.response import Response
from SerializerApp.models import Student
from SerializerApp.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

@api_view(['GET', 'POST'])
def HomeView(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    print('serializer :',serializer)
    print('serializer data :',serializer.data)
    return Response(serializer.data)