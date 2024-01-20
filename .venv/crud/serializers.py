from .models import Student
from .models import Teacher
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

      
class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'
      