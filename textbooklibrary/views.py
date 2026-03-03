from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def landing(request):
    return render(request, 'landing.html')

def time_table(request):
    return render(request, 'timetable.html')

def transcript(request):
    return render(request, 'transcript.html')
