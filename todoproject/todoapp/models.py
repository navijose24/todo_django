from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)

    def _str_(self):
        return self.title