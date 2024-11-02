from django.db import models

# Create your models here.

class Note(models.Model):
    pub_date = models.DateField()
    title = models.CharField(max_length=150)
    content = models.TextField()

