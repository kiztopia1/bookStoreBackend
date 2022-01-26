import imp
from django.contrib import admin

# Register your models here.
from .models import Book, Transaction
admin.site.register(Book)
admin.site.register(Transaction)