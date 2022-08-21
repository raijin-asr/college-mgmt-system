from django.urls import path
from registration.views import StudentListView, StudentAddView, StudentEditView, StudentDeleteView
from registration.teacher_views import TeacherListView, TeacherAddView, TeacherEditView, TeacherDeleteView
from registration.course_views import CourseListView, CourseAddView, CourseEditView, CourseDeleteView


urlpatterns = [
    #student url
    path('student/list', StudentListView.as_view(), name="StudentList"),
    path('student/add', StudentAddView.as_view(), name="StudentAdd"),
    path('student/edit/<student_id>',StudentEditView.as_view(), name="StudentEditGet"),
    path('student/edit', StudentEditView.as_view(), name="StudentEditPost"),
    path('student/delete/<student_id>',StudentDeleteView.as_view(), name="StudentDelete"),

    #teacher url
    path('teacher/list', TeacherListView.as_view(), name="TeacherList"),
    path('teacher/add', TeacherAddView.as_view(), name="TeacherAdd"),
    path('teacher/edit/<teacher_id>',TeacherEditView.as_view(), name="TeacherEditGet"),
    path('teacher/edit', TeacherEditView.as_view(), name="TeacherEditPost"),
    path('teacher/delete/<teacher_id>',TeacherDeleteView.as_view(), name="TeacherDelete"),

    #course url
    path('course/list', CourseListView.as_view(), name="CourseList"),
    path('course/add', CourseAddView.as_view(), name="CourseAdd"),
    path('course/edit/<course_id>',CourseEditView.as_view(), name="CourseEditGet"),
    path('course/edit', CourseEditView.as_view(), name="CourseEditPost"),
    path('course/delete/<course_id>',CourseDeleteView.as_view(), name="CourseDelete")
]
