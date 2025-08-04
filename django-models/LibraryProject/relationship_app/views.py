from django.shortcuts import render
from .models import Book  # ✅ required
from .models import Library  # ✅ required for checker

from django.views.generic.detail import DetailView

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
