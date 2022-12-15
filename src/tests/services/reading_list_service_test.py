import unittest
from services.reading_list_service import ReadingListService

class TestReadingListService(unittest.TestCase):
    def setUp(self):
        self.service = ReadingListService()

    def test_RLS_returns_correct_booktoread_object(self):
        result = self.service.add_readinglist_note("Soturikissat")

        assert result.description == "Soturikissat"
