from django.shortcuts import render
from django.views.generic import *
from myapp.models import Student
from django.urls import reverse_lazy

# Create your views here.
class StudentCreateView(CreateView):
    model=Student
    fields="__all__"

class StudentUpdateView(UpdateView) :
    model=Student
    fields=['Student_Name','Student_Marks']

class StudentListView(ListView):
    model = Student
   


class StudentDetailView(DetailView) :
    model=Student  

class StudentDeleteView(DeleteView):
    model=Student
    success_url=reverse_lazy('list')

