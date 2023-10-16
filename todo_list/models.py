from django.db import models

# Create your models here.
class Todo(models.Model):
    title: models.CharField = models.CharField(max_length=255)
    description: models.TextField = models.TextField()
    completed: models.BooleanField = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)