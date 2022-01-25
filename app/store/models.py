from tkinter import image_names
from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100, default='null')
    description =models.TextField(default='null')
    image_name = models.CharField(max_length=100, default='null')

    def __str__(self) :
        return self.name