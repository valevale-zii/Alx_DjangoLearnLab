# bookshelf/views.py

from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm

def book_search(request):
    """
    View to handle book search securely.

    - Uses BookSearchForm to validate and clean user input.
    - Uses Django ORM filter with parameterization to prevent SQL injection.
    - Renders 'book_list.html' with filtered books or empty list if no valid query.
    """
    form = BookSearchForm(request.GET or None)  # Bind form with GET data
    books = Book.objects.none()  # Empty queryset as default

    if form.is_valid():
        # Cleaned data is safe to use
        query = form.cleaned_data['query']

        # Filter books by title containing the query, case-insensitive
        # This uses parameterized queries internally to prevent SQL injection
        books = Book.objects.filter(title__icontains=query)

    return render(request, 'bookshelf/book_list.html', {
        'form': form,
        'books': books,
    })
