from django.forms import ModelForm, HiddenInput, RadioSelect, Select
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


RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'rating')
        widgets = {'rating': Select(choices=RATING_CHOICES)}