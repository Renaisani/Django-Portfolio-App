from django.shortcuts import render
from .models import Projects

# Create your views here.

def home(request):
    projects_data = Projects.objects.all()

    return render(request, "index.html", {"projects": projects_data})


def project_page(request, project_name):
    


def login(request):
    return render(request, "login.html")    