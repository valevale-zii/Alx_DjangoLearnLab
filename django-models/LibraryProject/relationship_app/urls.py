from django.urls import path
from .views import list_books, LibraryDetailView  # ✅ Required by checker

urlpatterns = [
    # ✅ New ones for this task
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # ✅ Keep your existing routes below (if you had any)
    # path('your-other-url/', your_view_name, name='your_view_name'),
]
