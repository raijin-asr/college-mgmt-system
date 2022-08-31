from django.shortcuts import render, redirect
from django.views.generic import View
from . models import Teacher, T_Assignment,Student, Assignment
from college_mgmt import auth_required
from user_mgmt.models import User


# Create your views here.
class TeacherHomeView(View):
    @auth_required
    def get(self, request, *args, **kwargs):
        context={ 
            "teacher_count": Teacher.objects.count(),
            "student_count": Student.objects.count(),
            "user_count": User.objects.count(),


        }
        return render(request, "registration/teacher_home.html",context)

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

# Assignment views of Teacher
class TeacherAssigSubmittedView(View):
    @auth_required
    def get(self, request):
        assignments=Assignment.objects.all()
        context = {
            "assignments" : assignments,
        }
        return render(request, "registration/teacher_home.html", context)
        
class TeacherAssigCreateView(View):
    @auth_required
    def get(self, request, *args, **kwargs):
        return render(request, "registration/teacher_home.html")

    @auth_required
    def post(self, request, *args, **kwargs):
        data = {
            "tassig_no": request.POST.get("tassig_no"),
            "tassig_question": request.POST.get("tassig_question"),
            "tassig_subject": request.POST.get("tassig_subject"),
            "tassig_date": request.POST.get("tassig_date"),
        } 
        tassignment=T_Assignment.objects.create(**data)
        tassignment.save()
        return redirect('/student/home')

class TeacherAssigSearchView(View):
    @auth_required
    def post(self, request, *args, **kwargs):
        tassig_subject = request.POST.get("tassig_subject", None)
        if not tassig_subject:
            result=T_Assignment.objects.all()
        else:   
            result = T_Assignment.objects.filter(tassig_subject__icontains = tassig_subject)
        context = {
            "tassignments" : result,
        }
        return render(request, "registration/student_home.html", context)

# class TeacherAssignShowView(View):
#     @auth_required
#     def get(self, request, *args, **kwargs):
#         url_parmeter = self.kwargs
#         tassig_id = url_parmeter["tassig_id"]
#         tassignment=T_Assignment.objects.get(tassig_id=tassig_id)
#         context = {
#             "tassignments" : tassignment,
#         }
#         return render(request, "registration/teacher_home.html", context)


# Apply for Leave views of Teacher
# class TeacherSubmitLeaveView(View):
#     @auth_required
#     def get(self, request, *args, **kwargs):
#         return render(request, "registration/teacher_home.html")

#     @auth_required
#     def post(self, request, *args, **kwargs):
#         data = {
#             "t_leave_name": request.POST.get("t_leave_name"),
#             "t_leave_type": request.POST.get("t_leave_type"),
#             "t_leave_days": request.POST.get("t_leave_days"),
#             "t_leave_reason": request.POST.get("t_leave_reason"),
#         } 
#         t_leave=T_Leave.objects.create(**data)
#         t_leave.save()
#         return redirect('/teacher/t_list_leave')


# class TeacherListLeaveView(View):
#     @auth_required
#     def get(self, request):
#         t_leaves=T_Leave.objects.all()
#         context = {
#             "teacher_leaves" : t_leaves,
#         }
#         return render(request, "registration/teacher_home.html", context)