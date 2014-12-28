from django.db import models


class Todo(models.Model):
    completed = models.BooleanField(default=False)
    name = models.CharField(max_length=1024)
