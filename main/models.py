from django.db import models

class Users(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=150)
    isactive = models.BooleanField(default=False)

    def __str__(self):
        return self.fullname
    

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(primary_key=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    cohort = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name