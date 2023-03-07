from django.shortcuts import render
from .models import Projects, ProjectEntry

# Create your views here.

def home(request):
    projects_data = Projects.objects.all()

    return render(request, "index.html", {"projects": projects_data})


def project_page(request, project_id=None):
    if project_id:
        project = Projects.objects.get(pk=project_id)
        project_entries = ProjectEntry.objects.filter(project_id=project_id)
        project_data = {"project": project, "project_entries": project_entries}
    else:
        project = {}

    return render(request, "project_page.html", project_data)



def login(request):
    return render(request, "login.html")    