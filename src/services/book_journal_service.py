from entities.book import Book
from repositories.book_journal_repository import book_journal_repository as bjr

class BookJournalService:
    """Lukupäiväkirjan sovelluslogiikasta vastaava luokka."""

    def __init__(self, book_journal_repository=bjr):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan
        palvelun.

        Args:
            book_journal_repository:
                BookJournalRepository-olio.
        """
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

        return books

book_journal_service = BookJournalService()
