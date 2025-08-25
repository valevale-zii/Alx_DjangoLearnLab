from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from api.models import Author, Book

class BookAPITest(TestCase):
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        # Initialize API client and log in
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass")
        
        # Create an author
        self.author = Author.objects.create(name="John Doe")

    def test_create_book(self):
        data = {
            "title": "Sample Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.post("/api/books/", data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "Sample Book")

    def test_list_books(self):
        Book.objects.create(title="Another Book", publication_year=2023, author=self.author)
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Another Book", str(response.data))
