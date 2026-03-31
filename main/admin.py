from django.contrib import admin

# Register your models here.
from .models import Users, Student
admin.site.register(Users)
admin.site.register(Student)