from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
   StuId=models.IntegerField(name="Student_ID")
   StuName=models.CharField(max_length=40,name="Student_Name")
   StuMarks=models.IntegerField(name="Student_Marks")
   def get_absolute_url(self):
      return reverse('list')
