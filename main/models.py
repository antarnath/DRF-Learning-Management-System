from django.db import models

# Create your models here.

# Teacher Model
class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=255)
    address = models.TextField()
    
    class Meta:
        verbose_name_plural = "1. Teachers"
    
# Course Category Model
class CourseCategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "2. Course Categories"
    
# Course Model
class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "3. Courses"
    
# Student Model
class Student(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=255)
    address = models.TextField()
    interested_categories = models.TextField()
    
    class Meta:
        verbose_name_plural = "4. Students"