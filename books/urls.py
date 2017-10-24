from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^authors/$', views.AuthorListView.as_view(), name="author_list"),
    url(r'^authors/(?P<author>[-\w]+)/$', views.AuthorDetailView.as_view(), name='author_detail'),
    url(r'^authors/(?P<author>[-\w]+)/update/$', views.AuthorUpdateView.as_view(), name='update_author'),
    url(r'^authors/create/new_author/$', views.AuthorFormView.as_view(), name='create_author'),
    url(r'^authors/(?P<author>[-\w]+)/delete/$', views.AuthorDeleteView.as_view(), name='delete_author'),

    url(r'^$', views.BookListView.as_view(), name="book_list"),
    url(r'^(?P<slug>[-\w]+)/$', views.BookDetailView.as_view(), name='book_detail'),
    url(r'^create/new_book/$', views.BookFormView.as_view(), name="create_book"),

    url(r'^category/(?P<category>[-\w]+)/$', views.CategoryDetailView.as_view(), name='category_detail'),
    url(r'^category/create/new_category/$', views.CategoryFormView.as_view(), name="create_category"),

]
