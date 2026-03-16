from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks"
    )

    def __str__(self):
        return self.title


class Category(models.Model):

    TEMPLATE_CHOICES = [
        ("anime", "Anime"),
        ("books", "Books"),
        ("movies", "Movies"),
        ("custom", "Custom"),
    ]

    name = models.CharField(max_length=100)

    template = models.CharField(
        max_length=20, choices=TEMPLATE_CHOICES, default="custom"
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="categories"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=255)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="statuses"
    )

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class ListObject(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    favorite = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    started_at = models.DateField(null=True, blank=True)
    finished_at = models.DateField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_objects"
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        related_name="list_objects",
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


@receiver(post_save, sender=Category)
def create_default_statuses(sender, instance, created, **kwargs):

    if created:

        if instance.template == "anime":
            statuses = ["Watching", "Completed", "Planned", "Dropped"]

        elif instance.template == "books":
            statuses = ["Reading", "Finished", "Want to read"]

        elif instance.template == "movies":
            statuses = ["Watched", "Plan to watch"]

        else:
            statuses = []

        for status in statuses:
            Status.objects.create(name=status, category=instance)
