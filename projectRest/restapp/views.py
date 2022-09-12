import imp
from django.shortcuts import render
from rest_framework.response import Response

from .models import Student
from django.contrib.auth.models import User
from .serializers import SignupSerializer, StudentSerializers

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication


# Create your views here.




@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
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



# for single data 
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def student_edit(request,id):
    try:
        student = Student.objects.get(pk = id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,template_name="<html>hello</html>",data="The Data you are looking for its not present.")


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




class SignupApiView(APIView):
    
    def get(self,request):
        users = User.objects.all()
        serializer = SignupSerializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    
    def post(self,request):
        try:
            serializer = SignupSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST,data="Bad Request")


#     def delete(self,request):
#         pass