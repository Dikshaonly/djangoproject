from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('add-student/', postStudent),
    path('add-teacher/',postTeacher),
    path('get-student/',getStudent),
    path('get-teacher/',getTeacher),
    path('editstudent/<id>',editStudentData),
    path('updatestudent/<id>',updateStudentData),
    path('updateteacher/<id>',updateTeacherData),
    path('deletestudent/<id>',deleteStudentData),
    path('deleteteacher/<id>',deleteTeacherData)
]