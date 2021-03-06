from django.db import models
from django.utils import timezone
#to get the user model
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    class Meta:
        ordering = ['-date_posted']
    def __str__(self):
        return f'{self.title} By {self.author}'
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    