from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

# List all books
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"

# Show details of a single book
class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"

# Update a book
class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_year']  # adjust based on your model fields
    template_name = "book_form.html"
    success_url = reverse_lazy('book-list')

# Delete a book
class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_confirm_delete.html"
    success_url = reverse_lazy('book-list')
