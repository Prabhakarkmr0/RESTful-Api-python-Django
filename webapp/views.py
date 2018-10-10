from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import  employeesSerializer

class employeeList(APIView):

    def get(self,request,format=None):
        employees1 = employees.objects.all()
        serializer = employeesSerializer(employees1, many=True)

        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = employeesSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        employees1 = employees.get_object(pk)
        employees1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class empdetail(APIView):
    def get_object(self,pk):
        try:
            return employees.objects.get(pk=pk)
        except employees.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk,format=None):
        employees1=self.get_object(pk)
        employees1=employeesSerializer(employees1)
        return Response(employees1.data)

    def put(self,request,pk,format=None):
        employees1= self.get_object(pk)
        serializer=employeesSerializer(employees1,data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        employees1=self.get_object(pk)
        employees1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)