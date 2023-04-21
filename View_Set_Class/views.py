from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from View_Set_Class.serializers import StudentSerializer
from View_Set_Class.models import Student
# Create your views here.


class HomeView(viewsets.ViewSet):
    def list(self, request, pk=None):
        print('**********list****************')
        print('basename :', self.basename)
        print('Action :', self.action)
        print('detail :', self.detail)
        print('suffix :', self.suffix)
       
        print('name :', self.name)
        print('description :', self.description)

        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    def create(self, request):
        print('**********create****************')
        print('basename :', self.basename)
        print('Action :', self.action)
        print('detail :', self.detail)
        print('suffix :', self.suffix)
       
        print('name :', self.name)
        print('description :', self.description)

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print('**********retrieve****************')
        print('basename :', self.basename)
        print('Action :', self.action)
        print('detail :', self.detail)
        print('suffix :', self.suffix)
        print('name :', self.name)
        print('description :', self.description)

        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Exception as e:
            return Response('Data Not Found')

    def update(self, request, pk):
        print('**********update****************')
        print('basename :', self.basename)
        print('Action :', self.action)
        print('detail :', self.detail)
        print('suffix :', self.suffix)
        print('name :', self.name)
        print('description :', self.description)

        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Please Enter Valid Info')

    def partial_update(self, request, pk):
        print('**********partial_update****************')
        print('basename :', self.basename)
        print('Action :', self.action)
        print('detail :', self.detail)
        print('suffix :', self.suffix)
        print('name :', self.name)
        print('description :', self.description)

        student = Student.objects.get(pk=pk)
        serilaizer = StudentSerializer(student, request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data)
        return Response('Please Enter Valid Info')

    def destroy(self, request, pk):
        print('**********destroy****************')
        print('basename :', self.basename)
        print('Action :', self.action)
        print('detail :', self.detail)
        print('suffix :', self.suffix)
        print('name :', self.name)
        print('description :', self.description)

        student = Student.objects.get(pk=pk)
        student.delete()
        return Response('Successfully Delete')
       


'''
ViewSet Class:-
1. we can use router
2. it is not provite get(), post() and instead provide actions
    sach as list(), create()

    (a). list():- Get All Record
    (b). retrieve():-Get Single Record
    (c). update():-Create/Insert Record
    (d). partial-update():- update record partial
    (e). destroy()

'''
