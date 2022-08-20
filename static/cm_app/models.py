from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.BigAutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    gender = models.CharField(max_length=20)
    faculty = models.CharField(max_length=100)

    #table to be used in database
    class Meta:
        db_table = 'students'
        
         


    
