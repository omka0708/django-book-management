from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=75)
    year = models.IntegerField()
    ISBN = models.CharField(max_length=15)
