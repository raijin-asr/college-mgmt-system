from django.db import models

# Create your models here.
#for Student
class Student(models.Model):
    student_id = models.BigAutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    gender = models.CharField(max_length=20)
    faculty = models.CharField(max_length=100)

    #table to be used in database
    class Meta:
        db_table = 'students'


#For Teacher
class Teacher(models.Model):
    teacher_id = models.BigAutoField(primary_key=True)
    teacher_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    faculty = models.CharField(max_length=100)

    #table to be used in database
    class Meta:
        db_table = 'teachers'
        
         
#For Course
class Course(models.Model):
    course_id = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    c_code = models.CharField(max_length=100)
    c_teacher = models.CharField(max_length=20)
    faculty = models.CharField(max_length=100)

    #table to be used in database
    class Meta:
        db_table = 'courses'

#For Student Assignments
class Assignment(models.Model):
    assig_id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    assig_question = models.CharField(max_length=500)
    assig_subject = models.CharField(max_length=50)
    assig_no = models.CharField(max_length=10)
    assig_answer = models.CharField(max_length=1000)

    #table to be used in database
    class Meta:
        db_table = 'assignments'

#For Teacher Assignments
class T_Assignment(models.Model):
    tassig_id = models.BigAutoField(primary_key=True)
    tassig_no = models.CharField(max_length=10)
    tassig_question = models.CharField(max_length=500)
    tassig_subject = models.CharField(max_length=50)
    tassig_date = models.CharField(max_length=100)

    #table to be used in database
    class Meta:
        db_table = 'tassignments'

#For Student Leave
class S_Leave(models.Model):
    s_leave_id = models.BigAutoField(primary_key=True)
    s_leave_name = models.CharField(max_length=100)
    s_leave_type = models.CharField(max_length=100)
    s_leave_days = models.CharField(max_length=50)
    s_leave_reason= models.CharField(max_length=200)

    #table to be used in database
    class Meta:
        db_table = 'student_leaves'

# #For Teacher Leave
class T_Leave(models.Model):
    t_leave_id = models.BigAutoField(primary_key=True)
    t_leave_name = models.CharField(max_length=100)
    t_leave_type = models.CharField(max_length=100)
    t_leave_days = models.CharField(max_length=50)
    t_leave_reason= models.CharField(max_length=200)

    #table to be used in database
    class Meta:
        db_table = 'teacher_leaves'
                 
                


    
