from . import views
from django.urls import path

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('forgetpass/', views.forgetpass, name='forgetpass'),
    path('dashboard/', views.index, name='index'),
    path('signout/', views.signout, name='signout'),
    path('dashboard/manage-students/', views.manage_students, name='manage_students'),
    path('dashboard/new-student/', views.newstudent, name='newstudent'),
    path('dashboard/deletestudent/<str:student_name>/', views.deletestudent, name='deletestudent'),
]