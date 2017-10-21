from django.forms import ModelForm
from .models import Book


class CreateBookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ['preview_image', 'slug']