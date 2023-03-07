from django.urls import path
from . import views


#App level url configs

urlpatterns = [
    path("", views.home, name="home"), #url for the home page
    path("projects/<int:project_id>", views.project_page, name="project_page"),
    path("login/", views.login, name="login"),
]