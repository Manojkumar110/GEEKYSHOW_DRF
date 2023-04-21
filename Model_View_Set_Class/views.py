from django.shortcuts import render
from rest_framework import viewsets
from Model_View_Set_Class.serializers import StudentSerializer
from Model_View_Set_Class.models import Student
# Create your views here.

'''
1. ModelViewSet:- It is provide Crud Operations
2. ReadOnlyModelViewSet:- It is provide get() & retrieve()
'''
# class HomeView(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer



class HomeView(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer