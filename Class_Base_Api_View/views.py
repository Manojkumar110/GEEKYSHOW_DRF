from rest_framework.views import APIView
from rest_framework.response import Response
from Class_Base_Api_View.serializers import StudentSerializer
from rest_framework import status
from Class_Base_Api_View.models import Student
# Create your views here.


class HomeView(APIView):
    def get(self, request, pk=None):
        if pk == None:
            student  = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data)
        else:
            try:
                student = Student.objects.get(pk=pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pass

    def patch(self, request):
        pass

    def delete(self, request):
        pass
