from django.urls import path
from .views import BookListCreateAPI, BookDetailAPI

urlpatterns = [
    path('books/', BookListCreateAPI.as_view(), name='api-book-list'),
    path('books/<int:pk>/', BookDetailAPI.as_view(), name='api-book-detail'),
]
