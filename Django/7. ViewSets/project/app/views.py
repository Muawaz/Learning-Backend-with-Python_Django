from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializer import StudentSerializer
from rest_framework.authentication import (
    BasicAuthentication, 
    SessionAuthentication, 
    TokenAuthentication)
from rest_framework.permissions import (
    AllowAny, 
    IsAuthenticated, 
    IsAdminUser)

# Create your views here.

class StudentModelViewSet (viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
