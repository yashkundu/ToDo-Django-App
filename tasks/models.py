from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    text = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('tasks:detail', kwargs={'pk':self.pk})
