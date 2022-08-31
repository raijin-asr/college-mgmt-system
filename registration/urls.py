from django.urls import path
from registration.views import (StudentListView, StudentAddView, StudentEditView, StudentDeleteView, StudentSearchView,
    StudentHomeView, StudentAssigSubmitView,StudentAssigListView,StudentAssigSearchView)
from registration.teacher_views import (TeacherListView, TeacherAddView, TeacherEditView, TeacherDeleteView,TeacherSearchView,
    TeacherHomeView,TeacherAssigCreateView,TeacherAssigSubmittedView,TeacherAssigSearchView)
from registration.course_views import CourseListView, CourseAddView, CourseEditView, CourseDeleteView, CourseSearchView


urlpatterns = [
    #student url
    path('student/home', StudentHomeView.as_view(), name="StudentHome"),
    path('student/list', StudentListView.as_view(), name="StudentList"),
    path('student/add', StudentAddView.as_view(), name="StudentAdd"),
    path('student/edit/<student_id>',StudentEditView.as_view(), name="StudentEditGet"),
    path('student/edit', StudentEditView.as_view(), name="StudentEditPost"),
    path('student/delete/<student_id>',StudentDeleteView.as_view(), name="StudentDelete"),
    path('student/search',StudentSearchView.as_view(), name="StudentSearch"),
    path('student/submit_assignment',StudentAssigSubmitView.as_view(), name="StudentSubmitAssignment"),
    path('student/todo_assignment',StudentAssigListView.as_view(), name="StudentTodoAssignment"),
    path('student/search_assigment',StudentAssigSearchView.as_view(), name="StudentSearchAssignment"),
    # path('student/s_submit_leave',StudentSubmitLeaveView.as_view(), name="StudentSubmitLeave"),
    # path('student/s_list_leave',StudentListLeaveView.as_view(), name="StudentListLeave"),


    #teacher url
    path('teacher/home', TeacherHomeView.as_view(), name="TeacherHome"),
    path('teacher/list', TeacherListView.as_view(), name="TeacherList"),
    path('teacher/add', TeacherAddView.as_view(), name="TeacherAdd"),
    path('teacher/edit/<teacher_id>',TeacherEditView.as_view(), name="TeacherEditGet"),
    path('teacher/edit', TeacherEditView.as_view(), name="TeacherEditPost"),
    path('teacher/delete/<teacher_id>',TeacherDeleteView.as_view(), name="TeacherDelete"),
    path('teacher/search',TeacherSearchView.as_view(), name="TeacherSearch"),
    path('teacher/create_assignment',TeacherAssigCreateView.as_view(), name="TeacherCreateAssignment"),
    path('teacher/submitted_assignment',TeacherAssigSubmittedView.as_view(), name="TeacherSubmittedAssignment"),
    path('teacher/search_tassignment',TeacherAssigSearchView.as_view(), name="TeacherSearchAssignment"),
    # path('teacher/show_assignment/<tassig_id>',TeacherAssignShowView.as_view(), name="TeacherShowGetAssignment"),
    # path('teacher/show_tassignment',TeacherAssignShowView.as_view(), name="TeacherShowAssignment"),
    # path('teacher/t_submit_leave',TeacherSubmitLeaveView.as_view(), name="TeacherSubmitLeave"),
    # path('teacher/t_list_leave',TeacherListLeaveView.as_view(), name="TeacherListLeave"),


    #course url
    path('course/list', CourseListView.as_view(), name="CourseList"),
    path('course/add', CourseAddView.as_view(), name="CourseAdd"),
    path('course/edit/<course_id>',CourseEditView.as_view(), name="CourseEditGet"),
    path('course/edit', CourseEditView.as_view(), name="CourseEditPost"),
    path('course/delete/<course_id>',CourseDeleteView.as_view(), name="CourseDelete"),
    path('course/search',CourseSearchView.as_view(), name="CourseSearch")
]
