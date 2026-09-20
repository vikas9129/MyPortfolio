from django.contrib import admin

from .models import Profile, ProjectImage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "headline", "updated_at")


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "display_order", "created_at")
    list_filter = ("category",)
    ordering = ("category", "display_order", "-created_at")
