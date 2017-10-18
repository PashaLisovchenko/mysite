from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^authors/$', views.author_list, name="author_list"),
    url(r'^authors/(?P<author>[-\w]+)/$', views.author_detail, name='author_detail'),

    url(r'^$', views.book_list, name="book_list"),
    url(r'^(?P<book>[-\w]+)/$', views.book_detail, name='book_detail'),

    url(r'^category/(?P<category>[-\w]+)/$', views.category_detail, name='category_detail'),
    url(r'^category/create/new_category$', views.create_category, name="create_category"),

]
