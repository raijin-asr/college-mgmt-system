from django.shortcuts import render, redirect
from django.views.generic import View
from . models import Course
from college_mgmt import auth_required

# Create your views here.
class CourseListView(View):
    @auth_required
    def get(self, request):
        courses=Course.objects.all()
        context = {
            "courses" : courses
        }
        return render(request, "registration/course_list.html", context)

class CourseAddView(View):
    @auth_required
    def get(self, request, *args, **kwargs):
        return render(request, "registration/course_add.html")

    @auth_required
    def post(self, request, *args, **kwargs):
        data = {
            "course_name": request.POST.get("course_name"),
            "c_code": request.POST.get("c_code"),
            "c_teacher": request.POST.get("c_teacher"),
            "faculty": request.POST.get("faculty"),
        } 
        course=Course.objects.create(**data)
        course.save()
        return redirect('/course/list')


class CourseEditView(View):
    @auth_required
    def get(self, request, *args, **kwargs):
        url_parmeter = self.kwargs
        course_id = url_parmeter["course_id"]
        course=Course.objects.get(course_id=course_id)
        context = {
            "course" : course
        }
        return render(request, "registration/course_edit.html", context)
    
    @auth_required
    def post(self, request, *args, **kwargs):
        data = {
            "course_name": request.POST.get("course_name"),
            "c_code": request.POST.get("c_code"),
            "c_teacher": request.POST.get("c_teacher"),
            "faculty": request.POST.get("faculty"),
        } 
        Course.objects.filter(course_id = request.POST.get("course_id")).update(**data)
        return redirect('/course/list')


class CourseDeleteView(View):
    @auth_required
    def get(self, request, *args, **kwargs):
        url_parmeter = self.kwargs
        course_id = url_parmeter["course_id"]
        Course.objects.filter(course_id = course_id).delete()
        return redirect("/course/list")
    
class CourseSearchView(View):
    @auth_required
    def post(self, request, *args, **kwargs):
        course_name = request.POST.get("course_name", None)
        result = Course.objects.filter(course_name__icontains = course_name)
        context = {
            "courses" : result,
        }
        return render(request, "registration/course_list.html", context)