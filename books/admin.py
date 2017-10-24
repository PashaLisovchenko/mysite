from django.contrib import admin
from .models import Book, Author, Category, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'bio', 'date')


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'year', 'category')


admin.site.register(Book, BookAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'book', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Comment, CommentAdmin)