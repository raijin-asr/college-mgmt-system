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
                 


    
