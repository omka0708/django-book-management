from rest_framework import generics, permissions
from books.models import Book
from books.serializers import BookSerializer


class BookListAPI(generics.ListCreateAPIView):
    # View for adding and reading books (GET/POST)
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # View for reading, changing and deleting books (GET/PUT/PATCH/DELETE)
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
