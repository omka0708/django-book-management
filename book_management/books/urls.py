from django.urls import path
from books.views import BookListAPI, BookDetailAPI

urlpatterns = [
    path('api/books/', BookListAPI.as_view(), name='book-list'),
    path('api/books/<int:pk>', BookDetailAPI.as_view(), name='book-detail'),
]
