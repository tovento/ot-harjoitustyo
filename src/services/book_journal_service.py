from entities.book import Book
from entities.book_to_read import BookToRead
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

    def add_readinglist_note(self, description):
        """Lisää muistiinpanon lukulistalle."""
        note = BookToRead(description)

        self._book_journal_repository.save_note(note)

        return note

    def find_all_notes(self):
        """Hakee listan lukulistaan tallennetuista muistiinpanoista."""
        notes = self._book_journal_repository.find_all_notes()

        return notes

    def delete_note(self, note_id):
        """Poistaa yksittäisen muistiinpanon lukulistalta."""
        self._book_journal_repository.delete_note(note_id)

book_journal_service = BookJournalService()
