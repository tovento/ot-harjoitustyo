from entities.book import Book
from repositories.book_journal_repository import book_journal_repository as bjr

class BookJournalService:
    """ TODO """

    def __init__(self, book_journal_repository=bjr):
        """ TODO"""
        self._book_journal_repository = book_journal_repository

    def add_read_book(self, date, title, author, pages, notes=None):
        """Lisää uuden luetun kirjan lukupäiväkirjaan."""
        book = Book(
                date=date,
                title=title,
                author=author,
                pages=pages,
                notes=notes)

        self._book_journal_repository.save_book(book)

        return book

    def find_all_books(self):
        """Hakee listan Lukupäiväkirjaan tallennetuista luetuista kirjoista."""
        books = self._book_journal_repository.find_all()

book_journal_service = BookJournalService()
