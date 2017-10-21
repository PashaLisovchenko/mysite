from celery import shared_task
from io import BytesIO
from books.models import Book
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


@shared_task
def preview_image(book_id):
    book = Book.objects.get(pk=book_id)
    if book.image:
        size = 200, 400
        im = Image.open(book.image.path)
        im.thumbnail(size)
        temp_handle = BytesIO()
        im.save(temp_handle, 'jpeg')
        temp_handle.seek(0)
        print('preview image load...')
        suf = SimpleUploadedFile(str(book.id)+'.jpeg', temp_handle.read(), content_type='image/jpeg')
        book.preview_image.save(str(book.id)+'.jpeg', suf, save=True)
        print('successfully')