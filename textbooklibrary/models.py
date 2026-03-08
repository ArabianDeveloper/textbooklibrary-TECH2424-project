from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=150)
    credits = models.IntegerField()
    semester = models.CharField(max_length=50)


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    enrollment_year = models.IntegerField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)