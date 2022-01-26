from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from .models import Book, Transaction
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

def order_view(request, id):
    print(request.user.id)
    book = Book.objects.get(id=id)
    transaction = Transaction( bookId=book, userId=request.user )
    print(transaction)
    transaction.save()
    return redirect('/')