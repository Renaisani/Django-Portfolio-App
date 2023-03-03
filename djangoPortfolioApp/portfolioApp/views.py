from django.shortcuts import render
from .models import Projects, ProjectEntry

# Create your views here.

def home(request):
    projects_data = Projects.objects.all()

    return render(request, "index.html", {"projects": projects_data})


def project_page(request, project_name=""):
    if project_name:
        project = Projects.objects.get(title=project_name)
        project_entries = ProjectEntry.objects.filter(project_name=project_name)
        project_data = {"project": project, "project_entries": project_entries}
    else:
        project = {}

    return render(request, "project_page.html", project_data)



def login(request):
    return render(request, "login.html")    