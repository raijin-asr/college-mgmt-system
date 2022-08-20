from django.urls import path
from cm_app.views import StudentListView, StudentAddView, StudentEditView, StudentDeleteView

urlpatterns = [
   path('student/list',StudentListView.as_view(),name="StudentList"),
   path('student/add',StudentAddView.as_view(),name="StudentAdd"),
   path('student/edit/<student_id>',StudentEditView.as_view(),name="StudentEditGet"),
   path('student/edit',StudentEditView.as_view(),name="StudentEditPost"),
   path('student/delete/<student_id>',StudentDeleteView.as_view(),name="StudentDelete")
]