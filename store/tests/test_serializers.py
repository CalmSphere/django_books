from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Book
from store.serializers import BooksSerializer


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        test_user_1 = User.objects.create(username="test_username_1")
        test_user_2 = User.objects.create(username="test_username_2")

        book_1 = Book.objects.create(name="Test book 1", price=25,
                                     author_name="Author 1", owner=test_user_1)
        book_2 = Book.objects.create(name="Test book 2", price=55,
                                     author_name="Author 2", owner=test_user_2)

        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': "Test book 1",
                'price': "25.00",
                "author_name": "Author 1",
                "owner": book_1.owner.id
            },
            {
                'id': book_2.id,
                'name': "Test book 2",
                'price': "55.00",
                "author_name": "Author 2",
                "owner": book_2.owner.id
            },
        ]
        self.assertEqual(expected_data, data)
