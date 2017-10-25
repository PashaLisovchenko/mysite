from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db.models import signals, Avg
from django.dispatch import receiver


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
    avg_rating = models.FloatField(default=0)

    class Meta:
        ordering = ["-avg_rating"]

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


class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    rating = models.IntegerField(default=0)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.book)


@receiver(signals.post_save, sender = Comment)
def add_rating(instance, **kwargs):
    book = instance.book
    avg = book.comments.filter(active=True).aggregate(Avg('rating'))
    book.avg_rating = avg['rating__avg']
    book.save()