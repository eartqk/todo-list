from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=128)
    completed = models.BooleanField(default=False, blank=False, null=True)

    def __str__(self):
        return self.title