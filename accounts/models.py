from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True,
    )

    age = models.IntegerField(
        blank=True,
        null=True,
        )
    def __str__(self):
        return self.username