from django.db import models
from django.urls import reverse

from django.conf import settings


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks', on_delete=models.CASCADE, blank=True, null=True)
    text = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('tasks:detail', kwargs={'pk':self.pk})
