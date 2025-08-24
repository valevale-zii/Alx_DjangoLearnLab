from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Author, Book


class BookAPITests(APITestCase):
    def setUp(self):
        # Auth user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.force_authenticate(user=self.user)

        # Data
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        self.book1 = Book.objects.create(title="Book A", author=self.author1, publication_year=2001)
        self.book2 = Book.objects.create(title="Book B", author=self.author2, publication_year=1999)
        self.book3 = Book.objects.create(title="Another Book", author=self.author1, publication_year=2010)

        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book1.id])

    def test_list_books(self):
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp.data), 1)

    def test_retrieve_book(self):
        resp = self.client.get(self.detail_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["title"], self.book1.title)

    def test_create_book(self):
        data = {"title": "New Book", "author": self.author1.id, "publication_year": 2022}
        resp = self.client.post(self.list_url, data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_update_book(self):
        data = {"title": "Updated Title", "author": self.author1.id, "publication_year": 2020}
        resp = self.client.put(self.detail_url, data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        resp = self.client.delete(self.detail_url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_filter_by_author(self):
        resp = self.client.get(self.list_url, {"author": self.author1.id})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        for item in resp.data:
            self.assertEqual(item["author"], self.author1.id)

    def test_search_by_title(self):
        resp = self.client.get(self.list_url, {"search": "Another"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(any(b["title"] == "Another Book" for b in resp.data))

    def test_order_by_publication_year(self):
        resp = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        years = [b["publication_year"] for b in resp.data]
        self.assertEqual(years, sorted(years))

    def test_unauthenticated_cannot_create(self):
        # remove auth
        self.client.force_authenticate(user=None)
        data = {"title": "Nope", "author": self.author1.id, "publication_year": 2024}
        resp = self.client.post(self.list_url, data)
        self.assertIn(resp.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))
