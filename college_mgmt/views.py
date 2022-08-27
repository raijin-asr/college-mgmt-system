from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return render(request, "contact_us.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact_us.html")
        
def admin_home(request):
    return render(request, "admin_home.html")