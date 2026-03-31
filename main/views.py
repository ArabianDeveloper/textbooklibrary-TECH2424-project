from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Users , Student

def signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = Users.objects.get(email=email)
            if check_password(password, user.password):
                request.session["user_email"] = user.email
                request.session["user_name"] = user.fullname
                return redirect("index")
            else:
                return render(request, "auth/signin.html", {"alert": "Invalid password"})
        except Users.DoesNotExist:
            return render(request, "auth/signin.html", {"alert": "User not found"})
    return render(request, "auth/signin.html")

def signup(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = Users(fullname=fullname,email=email,password=make_password(password))
        user.save()
        return redirect("signin")
    return render(request, 'auth/signup.html')


def forgetpass(request):
    return render(request, 'auth/forgot-password.html')
def index(request):
    return render(request, 'dashboard/index.html')

def signout(request):
    request.session.flush()
    return redirect("signin")

def newstudent(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        cohort = request.POST.get("cohort")
        department = request.POST.get("department")
        major = request.POST.get("major")
        student = Student(name=name, email=email, phone=phone, address=address,
        cohort=cohort, department=department, major=major)
        student.save()
    return render(request, 'dashboard/new-student.html')