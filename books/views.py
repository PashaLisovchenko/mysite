from django.shortcuts import render, get_object_or_404
from .models import Book, Category


def list(request):
    book = Book.objects.all()
    context = {
        'books': book,
        'section': 'books',
    }
    return render(request, 'list_book.html', context)


def create_category(request):
    if request.method == 'POST':
        Category.objects.create(name=request.POST['title'])
    cat = Category.objects.all()
    context = {
        'cat': cat,
    }
    return render(request, 'create_category.html', context)


def book_detail(request, book):
    book = get_object_or_404(Book, slug=book)
    context = {
        'book': book,
    }
    return render(request, 'detail.html', context)
