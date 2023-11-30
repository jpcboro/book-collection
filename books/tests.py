from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title="book title",
            subtitle="book subtitle",
            author="Book Author",
            isbn="1234567890123",
        )

    def test_book_details(self):
        self.assertEqual(self.book.title, "book title")
        self.assertEqual(self.book.subtitle, "book subtitle")
        self.assertEqual(self.book.author, "Book Author")
        self.assertEqual(self.book.isbn, "1234567890123")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "book title")
        self.assertTemplateUsed(response, "books/book_list.html")
