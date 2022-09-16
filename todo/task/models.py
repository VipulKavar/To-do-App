from django.utils import timezone
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    task_content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title