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

def books(request):
    return render(request, 'books.html')

def contact(request):
    return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')

def library(request):
    return render(request, 'library.html')

def catalog(request):
    return render(request, 'catalog.html')

# accounts
def profile(request):
    return render(request, 'accounts/profile.html')

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def logout(request):
    return render(request, 'accounts/logout.html')
