import os
from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(upload_to='staticfiles/assets/', null=True)
    github_link = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title
    
    def get_image_name(self):
        return os.path.basename(self.project_image.name)
    

class ProjectEntry(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=255)
    post_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.post_title
    

class ContactEntry(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    company = models.CharField(max_length=100, null=True)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email