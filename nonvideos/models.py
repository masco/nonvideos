from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    iframe = models.CharField(max_length=1000)
    time = models.DateTimeField()
    views = models.IntegerField()
    index = models.BooleanField()
