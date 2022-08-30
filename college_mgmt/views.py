from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return render(request, "home.html")

def about_admin(request):
    return render(request, "about_admin.html")

def about_home(request):
    return render(request, "about_home.html")

def contact(request):
    return render(request, "contact_us_admin.html")
        
def admin_home(request):
    return render(request, "admin_home.html")

#  context={ 
#             "admin_count": User.objects.count()
#         }