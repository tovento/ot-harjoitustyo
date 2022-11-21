import unittest
from entities.book import Book
from services.book_journal_service import BookJournalService

class TestBookJournalService(unittest.TestCase):
    def setUp(self):
        self.service = BookJournalService()

    def test_BJS_returns_correct_object(self):
        result = self.service.add_read_book(
                                    "1.1.2022",
                                    "Bookname",
                                    "Great Author",
                                    123)

        assert result.date == "1.1.2022"
        assert result.title == "Bookname"
        assert result.author == "Great Author"
        assert result.pages == 123
        assert result.notes == None
