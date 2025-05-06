from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, '1_home.html')

def about(request):
    return render(request, '2_about_me.html')

def projects(request):
    return render(request, '3_projects.html')

def skills(request):
    return render(request, '4_skills.html')

def resume(request):
    return render(request, '5_resume.html')

def contact(request):
    return render(request, '6_contact.html')