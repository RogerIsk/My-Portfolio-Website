from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home_link'),
    path('about', views.about, name='about_link'),
    path('projects', views.projects, name='projects_link'),
    path('skills', views.skills, name='skills_link'),
    path('resume', views.resume, name='resume_link'),
    path('contact', views.contact, name='contact_link'),
]
