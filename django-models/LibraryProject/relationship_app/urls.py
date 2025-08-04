from django.urls import path
from .views import book_list, LibraryDetailView  # ✅ correct import

urlpatterns = [
    path('books/', book_list, name='book_list'),  # ✅ function-based view
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # ✅ class-based view
]
