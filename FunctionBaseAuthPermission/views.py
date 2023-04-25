from rest_framework.views import APIView
from rest_framework.response import Response
from FunctionBaseAuthPermission.models import Student1, Student2
from FunctionBaseAuthPermission.serializers import StudentSerializer1, StudentSerializer2
# Create your views here.


class HomeView1(APIView):
    def get(self, request):
        if request.method == 'GET':
            stu1 = Student1.objects.all()
            serializer = StudentSerializer1(stu1, many=True)
            return Response(serializer.data)

    def post(self, request):
        serialzer1 = StudentSerializer1(data=request.data)
        if serialzer1:
            serialzer1.is_valid()
            serialzer1.save()
            return Response('Serializer 1 Valid ')
        return Response('Serializer Not Valid')


class HomeView2(APIView):
    def get(self, request):
        if request.method == 'GET':
            student2 = Student2.objects.all()
            serializer = StudentSerializer1(student2, many=True)
            return Response(serializer.data)

    def post(self, request):
        serialzer2 = StudentSerializer2(data=request.data)
        if serialzer2:
            serialzer2.is_valid()
            serialzer2.save()
            return Response('Serializer 2 Valid ')
        return Response('Serializer Not Valid')
