from django.shortcuts import render
from .models import Book
# Create your views here.

def home_view(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'store/home.html', context )


def book_detail_view(request,id):
    book = Book.objects.get(id=id)
    context = {
        'book': book
    }
    return render(request, 'store/book_details.html', context)