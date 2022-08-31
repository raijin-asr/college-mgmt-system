from django.shortcuts import render, redirect
from django.views.generic import View
from . models import Student, Assignment, T_Assignment
from college_mgmt import auth_required

# Create your views here.
class StudentHomeView(View):
    @auth_required
    def get(self, request, *args, **kwargs):
        context={ 
            "student_count": Student.objects.count()
        }
        return render(request, "registration/student_home.html",context)

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


# Assignment views of Student
class StudentAssigListView(View):
    @auth_required
    def get(self, request):
        tassignments=T_Assignment.objects.all()
        context = {
            "tassignments" : tassignments,
        }
        return render(request, "registration/student_home.html", context)
        
class StudentAssigSubmitView(View):
    @auth_required
    def get(self, request, *args, **kwargs):
        return render(request, "registration/student_home.html")

    @auth_required
    def post(self, request, *args, **kwargs):
        data = {
            "full_name": request.POST.get("full_name"),
            "assig_question": request.POST.get("assig_question"),
            "assig_subject": request.POST.get("assig_subject"),
            "assig_no": request.POST.get("assig_no"),
            "assig_answer": request.POST.get("assig_answer"),
        } 
        assignment=Assignment.objects.create(**data)
        assignment.save()
        redirect('/teacher/submitted_assignment')
        return render(request, "registration/student_home.html")


class StudentAssigSearchView(View):
    @auth_required
    def post(self, request, *args, **kwargs):
        assig_subject = request.POST.get("assig_subject", None)
        if not assig_subject:
            result=Assignment.objects.all()
        else:   
            result = Assignment.objects.filter(assig_subject__icontains = assig_subject)
        context = {
            "assignments" : result,
        }
        return render(request, "registration/teacher_home.html", context)

# Apply for Leave views of Student
# class StudentSubmitLeaveView(View):
#     @auth_required
#     def get(self, request, *args, **kwargs):
#         return render(request, "registration/student_home.html")

#     @auth_required
#     def post(self, request, *args, **kwargs):
#         data = {
#             "s_leave_name": request.POST.get("s_leave_name"),
#             "s_leave_type": request.POST.get("s_leave_type"),
#             "s_leave_days": request.POST.get("s_leave_days"),
#             "s_leave_reason": request.POST.get("s_leave_reason"),
#         } 
#         s_leave=S_Leave.objects.create(**data)
#         s_leave.save()
#         return redirect('/student/s_list_assignment')


# class StudentListLeaveView(View):
#     @auth_required
#     def get(self, request):
#         s_leaves=S_Leave.objects.all()
#         context = {
#             "student_leaves" : s_leaves,
#         }
#         return render(request, "registration/student_home.html", context)