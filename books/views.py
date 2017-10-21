from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category, Author
from .forms import CreateBookForm
from .tasks import preview_image


def book_list(request):
    book = Book.objects.all()
    context = {
        'books': book,
        'section': 'books',
    }
    return render(request, 'list_book.html', context)


def book_detail(request, book):
    book = get_object_or_404(Book, slug=book)
    context = {
        'book': book,
        'section': 'books',
    }
    return render(request, 'detail_book.html', context)


def create_book(request):
    if request.method == "POST":
        form = CreateBookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            # title = form.changed_data['title']
            form.save()
            # book = Book.objects.get(title=title)
            # preview_image.delay(book.id)
            return redirect("/books")
    else:
        form = CreateBookForm()
        context = {
            'form': form,
            'section': 'create_book',
        }
        return render(request, 'create_book.html', context)


def author_list(request):
    author = Author.objects.all()
    context = {
        'author': author,
        'section': 'author',
    }
    return render(request, 'list_author.html', context)


def author_detail(request, author):
    author = get_object_or_404(Author, slug=author)
    books = Book.objects.filter(author=author)
    context = {
        'books': books,
        'author': author,
        'section': 'author',
    }
    return render(request, 'detail_author.html', context)


def category_detail(request, category):
    category = get_object_or_404(Category, slug=category)
    books = Book.objects.filter(category=category)
    context = {
        'category': category,
        'books': books,
        'section': 'books',
    }
    return render(request, 'detail_category.html', context)


def create_category(request):
    if request.method == 'POST':
        Category.objects.create(name=request.POST['title'])
    context = {
        'section': 'create_category',
    }
    return render(request, 'create_category.html', context)
