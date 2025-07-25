from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def students(request):
    students = Student.objects.all()
    return render(request,'student_list.html',{"student":students})

def add_student(request):
    return render(request,'add_student.html')