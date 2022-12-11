import unittest
from entities.book import Book
from entities.book_to_read import BookToRead
from repositories.book_journal_repository import book_journal_repository

class TestBookJournalRepository(unittest.TestCase):
    def setUp(self):
        book_journal_repository.delete_all()
        self.book_x = Book("2.2.2022", "Title X", "Author X", 500, "Okay")
        self.book_y = Book("3.3.2022", "Title Y", "Author Y", 200, "Great")
        self.note1 = BookToRead("Sinuhe Egyptiläinen")
        self.note2 = BookToRead("Tatu ja Patu Helsingissä")


    def test_save_book(self):
        book_journal_repository.save_book(self.book_x)

        books = book_journal_repository.find_all()

        self.assertEqual(len(books), 1)

        self.assertEqual(books[0].date, self.book_x.date)
        self.assertEqual(books[0].title, self.book_x.title)
        self.assertEqual(books[0].author, self.book_x.author)
        self.assertEqual(books[0].pages, self.book_x.pages)
        self.assertEqual(books[0].notes, self.book_x.notes)

    def test_find_all(self): 
        book_journal_repository.save_book(self.book_x)
        book_journal_repository.save_book(self.book_y)

        books = book_journal_repository.find_all()

        self.assertEqual(len(books), 2)

        self.assertEqual(books[0].title, "Title X")
        self.assertEqual(books[1].title, "Title Y")

    def test_save_note(self):
        book_journal_repository.save_note(self.note1)

        notes = book_journal_repository.find_all_notes()

        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0][0].description, self.note1.description)

    def test_find_all_notes(self):
        book_journal_repository.save_note(self.note1)
        book_journal_repository.save_note(self.note2)

        notes = book_journal_repository.find_all_notes()
        
        self.assertEqual(len(notes), 2)

        self.assertEqual(notes[0][0].description, "Sinuhe Egyptiläinen")
        self.assertEqual(notes[1][0].description, "Tatu ja Patu Helsingissä")
