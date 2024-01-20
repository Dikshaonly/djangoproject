from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializers
from .serializers import TeacherSerializers
from .models import *
# Create your views here.
@api_view(['POST'])
def postStudent(request):   
    try:
     request_data=request.data
     serializer_std=StudentSerializers(data=request_data,many=False)
     if serializer_std.is_valid(raise_exception=True):
        serializer_std.save()
        return Response({'message':"student added succesfully"})
    except Exception as e:
     return Response({"err":e})
 
@api_view(['POST'])
def postTeacher(request):
    try:
        request_data=request.data
        serializer_tea=TeacherSerializers(data=request_data,many=False) 
        if serializer_tea.is_valid(raise_exception=True):
            serializer_tea.save()
            return Response({'message':"Teacher added sucessfully"})
    except Exception as e:
        return Response({"err":e})
    
@api_view(['GET'])
def getStudent(request):
    try:
        students=Student.objects.all()
        serialized_data=StudentSerializers(students,many=True)
        return Response(serialized_data.data)  
    except Exception as e:
        return Response({"err":e})
    
@api_view(['GET']) #information dinchha
def getTeacher(request):
    try:
        teachers=Teacher.objects.all()
        serialized_data=TeacherSerializers(teachers,many=True)
        return Response(serialized_data.data)
    except Exception as e:
        return Response ({"err":e})
    

        
@api_view(['GET']) #id enter garda tesko info dinchha
def editStudentData(request,id):
    student=Student.objects.get(id=id)
    serialized_data=StudentSerializers(student,many=False,)
    return Response(serialized_data.data)
        
@api_view(['POST']) #id bata aako info lai alter garna milxa
def updateStudentData(request,id):
    try:
      student=Student.objects.get(id=id)
      serialized_data=StudentSerializers(student,data=request.data,many=False,partial=True)
      if serialized_data.is_valid(raise_exception=True):
          serialized_data.save()
      return Response({"message":"Student Data has been Updated","data":serialized_data.data})
    except Exception as e:
      return Response({"err":e})
@api_view(['POST'])
def updateTeacherData(request,id):
    try:
        teacher=Teacher.objects.get(id=id)
        serialized_data=TeacherSerializers(teacher,data=request.data,many=False,partial=True)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
        return Response({"message":"Teacher Data has been Updated","data":serialized_data.data})
    except Exception as e:
        return Response({"err":e})
    
@api_view(['GET']) #id deyera delete garne
def deleteStudentData(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return Response({"message":'Student Data Deleted'})
@api_view(['GET'])
def deleteTeacherData(request,id):
    teacher=Teacher.objects.get(id=id)
    teacher.delete()
    return Response({"message":'Teacher Data Deleted'})