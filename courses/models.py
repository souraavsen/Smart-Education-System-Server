from pyexpat import model
from django.db import models

from accounts.models import StudentPorfile, TeacherPorfile
# Create your models here.

class Classes(models.Model):
    class_name = models.CharField(max_length=20)
    section = models.CharField(max_length=20)
    # students = models.ManyToManyField(StudentPorfile)


class Courses(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    course_code = models.CharField(max_length=100)
    classes = models.ManyToManyField(Classes)
    instructor = models.ForeignKey(TeacherPorfile, on_delete=models.CASCADE, null=True)

class CourseContent(models.Model):
    title = models.CharField(max_length=500)
    details = models.TextField()
    links = models.TextField()
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)

class CourseContentFile(models.Model):
    file = models.FileField()
    course_content = models.ForeignKey(CourseContent, on_delete=models.CASCADE)
    

