from django.test import TestCase
from django.urls import reverse

from .models import Book

class BookTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title = 'test book',
            author = 'test author',
            price = 20.00,
        )

    def test_string_representation(self):
        self.assertEqual(f'{self.book.title}', 'test book')
        self.assertEqual(f'{self.book.author}', 'test author')
        self.assertEqual('{:.2f}'.format(self.book.price), '20.00')
    
    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertContains(response, 'test book')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/123456')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'books/book_detail.html')
        self.assertContains(response, 'test book')
        self.assertNotContains(response, 'Hi there! this text should not be this page')