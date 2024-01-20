from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no=models.CharField(max_length=100)
    age=models.IntegerField()
    def __str__(self) -> str:
        return f"{self.name}"

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    subject=models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"{self.name}"
