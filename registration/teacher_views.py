from django.shortcuts import render, redirect
from django.views.generic import View
from . models import Teacher
from college_mgmt import auth_required

# Create your views here.
class TeacherListView(View):
    @auth_required
    def get(self, request):
        teachers=Teacher.objects.all()
        context = {
            "teachers" : teachers
        }
        return render(request, "registration/teacher_list.html", context)

class TeacherAddView(View):
    @auth_required
    def get(self, request, *args, **kwargs):
        return render(request, "registration/teacher_add.html")

    @auth_required
    def post(self, request, *args, **kwargs):
        data = {
            "teacher_name": request.POST.get("teacher_name"),
            "address": request.POST.get("address"),
            "gender": request.POST.get("gender"),
            "faculty": request.POST.get("faculty"),
        } 
        teacher=Teacher.objects.create(**data)
        teacher.save()
        return redirect('/teacher/list')


class TeacherEditView(View):
    @auth_required
    def get(self, request, *args, **kwargs):
        url_parmeter = self.kwargs
        teacher_id = url_parmeter["teacher_id"]
        teacher=Teacher.objects.get(teacher_id=teacher_id)
        context = {
            "teachers" : teacher
        }
        return render(request, "registration/teacher_edit.html", context)
    
    @auth_required
    def post(self, request, *args, **kwargs):
        data = {
            "teacher_name": request.POST.get("teacher_name"),
            "address": request.POST.get("address"),
            "gender": request.POST.get("gender"),
            "faculty": request.POST.get("faculty"),
        } 
        Teacher.objects.filter(teacher_id = request.POST.get("teacher_id")).update(**data)
        return redirect('/teacher/list')


class TeacherDeleteView(View):
    @auth_required
    def get(self, request, *args, **kwargs):
        url_parmeter = self.kwargs
        teacher_id = url_parmeter["teacher_id"]
        Teacher.objects.filter(teacher_id = teacher_id).delete()
        return redirect("/teacher/list")
    

class TeacherSearchView(View):
    @auth_required
    def post(self, request, *args, **kwargs):
        teacher_name = request.POST.get("teacher_name", None)
        result = Teacher.objects.filter(teacher_name__icontains = teacher_name)
        context = {
            "teachers" : result,
        }
        return render(request, "registration/teacher_list.html", context)

