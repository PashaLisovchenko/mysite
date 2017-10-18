from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    bio = models.TextField(max_length=248)
    date = models.DateField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Category(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=48)
    slug = models.SlugField(max_length=250,
                            blank=True)
    description = models.TextField(max_length=500)
    year = models.IntegerField()
    image = models.ImageField(blank=True,
                              upload_to='images/book/',
                              verbose_name='Ссылка картинки')
    author = models.ManyToManyField(Author)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book_detail',
                       args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Book, self).save(*args, **kwargs)
