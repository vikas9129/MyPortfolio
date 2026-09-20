from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile, ProjectImage


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "name",
            "headline",
            "bio",
            "profile_image",
            "hero_image",
            "instagram_url",
            "youtube_url",
            "email",
        )
        widgets = {"bio": forms.Textarea(attrs={"rows": 5})}


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ("title", "category", "image", "display_order")
