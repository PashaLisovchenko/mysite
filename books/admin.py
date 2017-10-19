from django.contrib import admin
from .models import Book, Author, Category


#@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Category, CategoryAdmin)

#@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'bio', 'date')
admin.site.register(Author, AuthorAdmin)

#@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'year', 'category')
admin.site.register(Book, BookAdmin)