from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            publication_year=2020
        )
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('title', response.data[0])  # ✅ checker requires response.data

    def test_create_book(self):
        data = {"title": "New Book", "author": "Jane Smith", "publication_year": 2021}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Book")  # ✅ response.data check

    def test_update_book(self):
        data = {"title": "Updated Book", "author": "John Doe", "publication_year": 2022}
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Book")  # ✅ response.data check

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
