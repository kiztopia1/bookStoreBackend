from datetime import date
from tkinter import image_names
from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=100, default='null')
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description =models.TextField(default='null')
    image_name = models.CharField(max_length=100, default='null')

    def __str__(self) :
        return self.title

class Transaction(models.Model):
    date = models.DateTimeField()
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE)
    userId = models.CharField(max_length=100)