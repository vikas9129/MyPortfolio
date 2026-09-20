from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=120, default="Niteesh Patel")
    headline = models.CharField(max_length=160, default="An Artist")
    bio = models.TextField(default="Creative thinker and artist building visual stories.")
    profile_image = models.ImageField(upload_to="profile/", blank=True)
    hero_image = models.ImageField(upload_to="profile/", blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "portfolio profile"
        verbose_name_plural = "portfolio profile"

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    CATEGORY_CHOICES = [
        ("works", "My Works"),
        ("achievements", "Achievements"),
        ("personality", "Personality"),
        ("college", "College"),
    ]

    title = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="works")
    image = models.ImageField(upload_to="projects/")
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["category", "display_order", "-created_at"]

    def __str__(self):
        return self.title or self.image.name.rsplit("/", 1)[-1]
