from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def login(request):
    return render(request,'account.html')

def students(request):
    students = Student.objects.all()
    return render(request,'student_list.html',{"student":students})