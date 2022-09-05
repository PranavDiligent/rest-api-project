from django.shortcuts import render
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializers

from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def student_list(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializers(students,many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = StudentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def student_edit(request,id):
    try:
        student = Student.objects.get(pk = id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method =="GET":
        serializer = StudentSerializers(student)
        return Response(serializer.data)

    if request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = StudentSerializers(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)