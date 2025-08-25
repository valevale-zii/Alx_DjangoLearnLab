from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Author, Book


class AuthorTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        # Create an author
        self.author = Author.objects.create(name="J.K. Rowling")

    def test_get_authors(self):
        response = self.client.get("/api/authors/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("name", response.data[0])


class BookTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="testuser2", password="testpass2")
        self.client.login(username="testuser2", password="testpass2")

        # Create an author and a book
        self.author = Author.objects.create(name="George R.R. Martin")
        self.book = Book.objects.create(
            title="A Game of Thrones", author=self.author
        )

    def test_get_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("title", response.data[0])
