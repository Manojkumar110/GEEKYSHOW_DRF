from django.db import models

# Create your models here.

class Student1(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    city = models.CharField(max_length=50)


class Student2(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    city = models.CharField(max_length=50)