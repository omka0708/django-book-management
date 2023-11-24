from rest_framework import generics, permissions
from books.models import Book
from books.serializers import BookSerializer


class BookListAPI(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
