import hashlib

from django.shortcuts import redirect, render
from django.views.generic import View
from django.http import HttpResponse
from . models import User

# Create your views here.
class UserLoginView(View):
    def get(self, request):
        return render(request, "user_mgmt/login.html")

    def post(self,request):
        #calculating hash of password
        password_hash = hashlib.sha256(request.POST.get("password").encode('utf-8')).hexdigest()
        user_name = request.POST.get("user_name")
        user = User.objects.filter(user_name = user_name, password = password_hash).first()
       
        #if only there is user data rows database
        if  user: 

            #setting data to django session named as current_user
            request.session["current_user"] = {
                "user_name":  user.user_name,
                "role": user.role
            }

            #redirect to student list if user name passoword is valid
            return redirect("/student/list")
 
        return  HttpResponse("<h1>Invalid User Name Password</h1>")

class UserLoginOutView(View):
    def get(self, request):
        request.session["current_user"] = None
        return redirect("/login")

class UserAddView(View): #sign UP
    def get(self, request, *args, **kwargs):
        return render(request, "user_mgmt/user_add.html")

    def post(self, request, *args, **kwargs):
        #calculating hash of password
        password_hash = hashlib.sha256(request.POST.get("password").encode('utf-8')).hexdigest()
        data = {
            "user_name": request.POST.get("user_name"),
            "password": password_hash,
            "role": request.POST.get("role")
        } 
        user = User.objects.create(**data)
        user.save()
        return redirect('/login')


