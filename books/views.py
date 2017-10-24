from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Book, Category, Author
from .forms import CreateBookForm, CreateCategoryForm, CreateAuthorForm
from django.views.generic import View, ListView, DetailView, CreateView,\
    FormView, UpdateView, DeleteView


class BookListView(ListView):
    template_name = 'list_book.html'
    model = Book
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['section'] = 'books'
        return context


class BookDetailView(DetailView):
    template_name = 'detail_book.html'
    model = Book
    context_object_name = 'book'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['section'] = 'books'
        return context


class BookFormView(CreateView):
    template_name = 'create_book.html'
    form_class = CreateBookForm

    def form_valid(self, form):
        form.save()
        return redirect('/books')

    def get_context_data(self, **kwargs):
        context = super(BookFormView, self).get_context_data(**kwargs)
        context['section'] = 'create_book'
        return context


class AuthorListView(ListView):
    template_name = 'list_author.html'
    model = Author
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['section'] = 'author'
        return context


class AuthorDetailView(DetailView):
    template_name = 'detail_author.html'
    model = Author
    context_object_name = 'author'
    slug_url_kwarg = 'author'

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        books = Book.objects.filter(author=context['author'])
        context['books'] = books
        context['section'] = 'author'
        return context


class AuthorFormView(CreateView):
    template_name = 'create_author.html'
    form_class = CreateAuthorForm

    def form_valid(self, form):
        form.save()
        return redirect('/books/authors')

    def get_context_data(self, **kwargs):
        context = super(AuthorFormView, self).get_context_data(**kwargs)
        context['section'] = 'create_author'
        return context


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = CreateAuthorForm
    template_name = 'update_author_form.html'
    slug_url_kwarg = 'author'
    success_url = '/books/authors/'

    def get_context_data(self, **kwargs):
        context = super(AuthorUpdateView, self).get_context_data(**kwargs)
        context['section'] = 'author'
        return context


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'delete_author.html'
    slug_url_kwarg = 'author'
    success_url = '/books/authors/'

    def get_context_data(self, **kwargs):
        context = super(AuthorDeleteView, self).get_context_data(**kwargs)
        context['section'] = 'author'
        return context


class CategoryDetailView(DetailView):
    template_name = 'detail_category.html'
    model = Category
    context_object_name = 'category'
    slug_url_kwarg = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        books = Book.objects.filter(category=context['category'])
        context['books'] = books
        context['section'] = 'books'
        return context


class CategoryFormView(CreateView):
    template_name = 'create_category.html'
    form_class = CreateCategoryForm

    def form_valid(self, form):
        form.save()
        return redirect('/books')

    def get_context_data(self, **kwargs):
        context = super(CategoryFormView, self).get_context_data(**kwargs)
        context['section'] = 'create_category'
        return context
