from django.contrib import admin
from .models import Projects, ProjectEntry, ContactEntry

# Register your models here.
admin.site.register(Projects)
admin.site.register(ProjectEntry)
admin.site.register(ContactEntry)