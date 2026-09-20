from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/profile/", views.profile_update, name="profile_update"),
    path("dashboard/projects/add/", views.project_create, name="project_create"),
    path("dashboard/projects/<int:pk>/delete/", views.project_delete, name="project_delete"),
]
