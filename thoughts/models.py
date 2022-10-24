from django.db import models


class Thought(models.Model):
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    likes = models.IntegerField()
    date = models.CharField(max_length=100)
