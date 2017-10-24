from django.forms import ModelForm, HiddenInput
from .models import Book, Category, Author, Comment


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


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        # widgets = {'book': HiddenInput()}