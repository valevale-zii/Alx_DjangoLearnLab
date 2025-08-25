from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Author, Book

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client = APIClient()

        # Log in the user
        self.client.login(username="testuser", password="testpassword")

        # Create sample Author and Book
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            author=self.author,
            publication_date="1997-06-26"
        )

    def test_book_list(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)

    def test_book_detail(self):
        response = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)
