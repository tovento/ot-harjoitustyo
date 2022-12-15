import unittest
from entities.book_to_read import BookToRead
from repositories.reading_list_repository import reading_list_repository
from repositories.book_journal_repository import book_journal_repository

class TestReadingListRepository(unittest.TestCase):
    def setUp(self):
        book_journal_repository.delete_all()
        self.note1 = BookToRead("Sinuhe Egyptiläinen")
        self.note2 = BookToRead("Tatu ja Patu Helsingissä")

    def test_save_note(self):
        reading_list_repository.save_note(self.note1)

        notes = reading_list_repository.find_all_notes()

        self.assertEqual(len(notes), 1)

        self.assertEqual(notes[0].description, self.note1.description)

    def test_find_all_notes(self):
        reading_list_repository.save_note(self.note1)
        reading_list_repository.save_note(self.note2)

        notes = reading_list_repository.find_all_notes()

        self.assertEqual(len(notes), 2)

        self.assertEqual(notes[0].description, "Sinuhe Egyptiläinen")
        self.assertEqual(notes[1].description, "Tatu ja Patu Helsingissä")

    def test_delete_note(self):
        reading_list_repository.save_note(self.note1)
        notes = reading_list_repository.find_all_notes()

        self.assertEqual(len(notes), 1)

        reading_list_repository.delete_note(1)
        notes = reading_list_repository.find_all_notes()

        self.assertEqual(len(notes), 0)
