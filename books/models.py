from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db.models import signals


class Author(models.Model):
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    slug = models.SlugField(max_length=250,
                            blank=True)
    bio = models.TextField(max_length=248)
    date = models.DateField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('books:author_detail',
                       args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name+' '+self.last_name)
        super(Author, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=48)
    slug = models.SlugField(max_length=250,
                            blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books:category_detail',
                       args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=48)
    slug = models.SlugField(max_length=250,
                            blank=True)
    description = models.TextField(max_length=500)
    year = models.IntegerField()
    image = models.ImageField(blank=True,
                              null=True,
                              upload_to='image/')
    preview_image = models.ImageField(blank=True,
                                      null=True,
                                      upload_to='preview/')
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


def post_save_book(sender, instance, signal, *args, **kwargs):
    from .tasks import preview_image
    if instance.image and not instance.preview_image:
        preview_image.delay(instance.pk)


signals.post_save.connect(post_save_book, sender=Book)