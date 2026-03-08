from django import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'instructor', 'credits', 'semester')
    search_fields = ('code', 'title', 'instructor')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'enrollment_year', 'course')
    search_fields = ('name', 'email')



admin.site.register(CourseAdmin)
admin.site.register(StudentAdmin)