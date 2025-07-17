from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    d = {"title":"Django",
         "user_name":"Rahul",
         "logedIn": True,
         "languages":["Python","java","html","CSS"]}
    return render(request,'index.html',d)

def about(request):
    return HttpResponse("This is about peage..")