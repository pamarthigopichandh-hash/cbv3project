from django.contrib import admin
from myapp.models import Student

# Register your models here.
class StudentAdminint(admin.ModelAdmin):
    list_display=['StuId','StuName','StuMarks']
    class Meta:
        model=Student
        fields='__all__'
