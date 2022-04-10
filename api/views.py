from django.shortcuts import render
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework import viewsets
# Create your views here.
class Employeelist(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer