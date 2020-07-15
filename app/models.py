from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class ExampleModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    when_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username}'s Profile"
