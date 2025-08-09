from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # Form logic to create book
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    # Form logic to edit book
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    # Logic to delete book
    pass

