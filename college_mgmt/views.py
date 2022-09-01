from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from college_mgmt import auth_required
from registration. models import Teacher,Student, Course, Assignment, T_Assignment
from user_mgmt. models import User



def index(request):
    return render(request, "home.html")

def about_admin(request):
    return render(request, "about_admin.html")

def about_home(request):
    return render(request, "about_home.html")

def contact(request):
    return render(request, "contact_us_admin.html")

class AdminHomeView(View):
    @auth_required        
    def get(self, request, *args, **kwargs):    
        context={ 
                "teacher_count": Teacher.objects.count(),
                "student_count": Student.objects.count(),
                "user_count": User.objects.count(),
                "course_count": Course.objects.count(),
                "assignment_count": Assignment.objects.count(),
                "tassignment_count": T_Assignment.objects.count(),


            }
        return render(request, "admin_home.html",context)

