from django.db import models


# Create your models here.

class Publisher(models.Model):
    p_name = models.CharField('出版社',max_length=32)

    def __str__(self):
        return self.p_name

class Book(models.Model):
    b_name = models.CharField('书名',max_length=32)
    pub = models.ForeignKey('Publisher', blank=True, null=True)

    def __str__(self):
        return self.b_name


class Author(models.Model):
    a_name = models.CharField('作者',max_length=32)
    books = models.ManyToManyField('Book', blank=True, null=True)

    def __str__(self):
        return self.a_name