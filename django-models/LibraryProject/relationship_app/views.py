from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-Based View: List all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: Show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
