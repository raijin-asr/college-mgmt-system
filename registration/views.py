from django.shortcuts import render, redirect
from django.views.generic import View
from . models import Student
from college_mgmt import auth_required

# Create your views here.
class StudentListView(View):
    @auth_required
    def get(self, request):
        students=Student.objects.all()
        context = {
            "students" : students
        }
        return render(request, "registration/student_list.html", context)

class StudentAddView(View):
    @auth_required
    def get(self, request, *args, **kwargs):
        return render(request, "registration/student_add.html")

    @auth_required
    def post(self, request, *args, **kwargs):
        data = {
            "student_name": request.POST.get("student_name"),
            "roll_no": request.POST.get("roll_no"),
            "gender": request.POST.get("gender"),
            "faculty": request.POST.get("faculty"),
        } 
        student=Student.objects.create(**data)
        student.save()
        return redirect('/student/list')


class StudentEditView(View):
    @auth_required
    def get(self, request, *args, **kwargs):
        url_parmeter = self.kwargs
        student_id = url_parmeter["student_id"]
        student=Student.objects.get(student_id=student_id)
        context = {
            "student" : student
        }
        return render(request, "registration/student_edit.html", context)
    
    @auth_required
    def post(self, request, *args, **kwargs):
        data = {
            "student_name": request.POST.get("student_name"),
            "roll_no": request.POST.get("roll_no"),
            "gender": request.POST.get("gender"),
            "faculty": request.POST.get("faculty"),
        } 
        Student.objects.filter(student_id = request.POST.get("student_id")).update(**data)
        return redirect('/student/list')


class StudentDeleteView(View):
    @auth_required
    def get(self, request, *args, **kwargs):
        url_parmeter = self.kwargs
        student_id = url_parmeter["student_id"]
        Student.objects.filter(student_id = student_id).delete()
        return redirect("/student/list")
    

class StudentSearchView(View):
    @auth_required
    def post(self, request, *args, **kwargs):
        student_name = request.POST.get("student_name", None)
        result = Student.objects.filter(student_name__icontains = student_name)
        context = {
            "students" : result,
        }
        return render(request, "registration/student_list.html", context)

#for pagination
# class Index(ListView):
#     model = Teachers
#     context_object_name = 'teachers'
#     paginate_by = 6
#     template_name = 'teacher_list.html'