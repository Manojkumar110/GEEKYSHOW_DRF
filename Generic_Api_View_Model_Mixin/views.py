from django.shortcuts import render
from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,\
      UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from Generic_Api_View_Model_Mixin.models import Student
from Generic_Api_View_Model_Mixin.serializers import StudentSerializer
# Create your views here.

# Generic Api View & Model Mixin

# class HomeView(APIView):
#     def get(self, request):
#         return Response('Generic Api View Model Mixin') 


'''
Generic Api View
1.ListModelMixin (get method)
2.CreateModelMixin (post method)
3.RetrieveModelMixin (get method)
4.UpdateModelMixin (put, patch method)

'''
class HomeView_List(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)
    
class HomeView_Create(GenericAPIView,CreateModelMixin):
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)
    
class HomeView_Update(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class HomeView_Retrive(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

class HomeView_Destroy(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def put(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
