from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileForm, ProjectImageForm, RegistrationForm
from .models import Profile, ProjectImage


def home(request):
    profile = Profile.objects.first()
    project_groups = [
        (category, ProjectImage.objects.filter(category=category))
        for category, _ in ProjectImage.CATEGORY_CHOICES
    ]
    return render(request, "portfolio/home.html", {"profile": profile, "project_groups": project_groups})


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard" if request.user.is_staff else "home")
    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your account is ready. An administrator can grant dashboard access.")
        return redirect("home")
    return render(request, "registration/register.html", {"form": form})


def staff_required(view):
    return user_passes_test(lambda user: user.is_active and user.is_staff, login_url="login")(view)


@staff_required
@login_required
def dashboard(request):
    profile = Profile.objects.first()
    projects = ProjectImage.objects.all()
    return render(request, "portfolio/dashboard.html", {"profile": profile, "projects": projects})


@staff_required
@login_required
def profile_update(request):
    profile = Profile.objects.first() or Profile()
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Profile details updated.")
        return redirect("dashboard")
    return render(request, "portfolio/profile_form.html", {"form": form})


@staff_required
@login_required
def project_create(request):
    form = ProjectImageForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project image uploaded.")
        return redirect("dashboard")
    return render(request, "portfolio/project_form.html", {"form": form})


@staff_required
@login_required
def project_delete(request, pk):
    project = get_object_or_404(ProjectImage, pk=pk)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project image removed.")
    return redirect("dashboard")
