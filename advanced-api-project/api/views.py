from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Book
from .serializers import BookSerializer

class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
