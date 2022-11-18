from entities.book import Book

class BookJournalService:
    """ TODO """

    def __init__(self):
        """ TODO"""
        pass

    def add_read_book(self, date, name, author, pages, notes=None):
        """Lisää uuden luetun kirjan lukupäiväkirjaan."""
        book = Book(
                date=date,
                name=name,
                author=author,
                pages=pages,
                notes=notes)

        return book
