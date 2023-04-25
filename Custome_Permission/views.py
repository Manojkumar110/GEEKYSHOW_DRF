from django.shortcuts import render
from rest_framework import viewsets
from Custome_Permission.models import Student
from Custome_Permission.serializers import StudentSerializers
from rest_framework.authentication import SessionAuthentication
from Custome_Permission.customepermission import MyPermission
# Create your views here.

class HomeView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    authentication_classes = [SessionAuthentication]
    # custome permission
    permission_classes = [MyPermission]