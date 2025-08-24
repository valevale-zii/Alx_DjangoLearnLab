from rest_framework import generics, filters
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Add filtering, ordering, searching
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ['title', 'author', 'publication_year']  # filtering
    ordering_fields = ['title', 'author', 'publication_year']  # ordering
    search_fields = ['title', 'author']  # searching

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
