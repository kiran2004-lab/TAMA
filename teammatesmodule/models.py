# teammatesmodule/models.py
from django.db import models
from django.core.exceptions import ValidationError

from django.core.exceptions import ValidationError

class PersonalTaskDetails(models.Model):
    Task_Title = models.CharField(max_length=255)
    Task_Priority = models.CharField(max_length=10, choices=[
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ], default='Medium')
    Start_Date = models.DateField()
    End_Date = models.DateField()
    Description = models.TextField()


    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Task_Title
