from django.db import models


# Create your models here.

class Publisher(models.Model):
    p_name = models.CharField(max_length=32)


class Book(models.Model):
    b_name = models.CharField(max_length=32)
    pub = models.ForeignKey('Publisher', blank=True, null=True)


class Author(models.Model):
    a_name = models.CharField(max_length=32)
    books = models.ManyToManyField('Book', blank=True, null=True)
