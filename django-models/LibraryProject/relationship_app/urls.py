from django.urls import path
from . import views  # ✅ for function-based views
from .views import LibraryDetailView  # ✅ for class-based views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]
