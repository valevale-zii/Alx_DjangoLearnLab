from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Author, Book

class AuthorBookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

        self.author = Author.objects.create(name="J.K. Rowling", bio="British author")
        self.book = Book.objects.create(
            title="Harry Potter",
            author=self.author,
            publication_date="1997-06-26"
        )

    def test_get_authors(self):
        response = self.client.get("/api/authors/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # ensure response contains expected data
        self.assertIn("name", response.data[0])

    def test_get_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("title", response.data[0])

    def test_create_author(self):
        response = self.client.post("/api/authors/", {"name": "George Orwell", "bio": "English novelist"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "George Orwell")

    def test_create_book(self):
        response = self.client.post("/api/books/", {
            "title": "1984",
            "author": self.author.id,
            "publication_date": "1949-06-08"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "1984")
