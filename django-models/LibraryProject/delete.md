from bookshelf.models import Book
b = Book.objects.get(title="1984")
b.delete()
Book.objects.all()
# Output: (1, {'bookshelf.Book': 1})
# Output: QuerySet []>
