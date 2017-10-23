from django.forms import ModelForm
from .models import Book, Category, Author


class CreateBookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ['preview_image', 'slug']


class CreateCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class CreateAuthorForm(ModelForm):
    class Meta:
        model = Author
        exclude = ['slug']