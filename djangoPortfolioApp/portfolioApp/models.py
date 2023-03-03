import os
from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(upload_to='portfolioApp/static/assets/', null=True)

    def __str__(self):
        return self.title
    
    def get_image_name(self):
        return os.path.basename(self.project_image.name)
    

class ProjectEntry(models.Model):
    project_name = models.ForeignKey(Projects, to_field="title", on_delete=models.CASCADE)
    post_title = models.CharField(max_length=255)
    post_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.post_title