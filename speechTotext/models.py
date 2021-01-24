from django.db import models
from django.utils import timezone

# Create your models here.

class Transcribe(models.Model):
    content = models.TextField()
    date_saved = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.content





