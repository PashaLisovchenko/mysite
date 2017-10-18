from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list, name="books"),
    url(r'^create_category/$', views.create_category, name="create_category"),
    url(r'^(?P<book>[-\w]+)/$', views.book_detail, name='book_detail'),
]
