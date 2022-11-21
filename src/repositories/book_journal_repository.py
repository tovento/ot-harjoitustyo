from entities.book import Book
from database_connection import get_database_connection

class BookJournalRepository:
    """TODO"""
    def __init__(self, connection):
        """TODO"""
        self._connection = connection

    def find_all(self):
        """Hakee kaikki tietokantaan tallennetut luetut kirjat."""
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Books")

        rows = cursor.fetchall()

        return [Book(
                    row["date"],
                    row["title"],
                    row["author"],
                    row["pages"],
                    row["notes"]) for row in rows]

    def save_book(self, book):
        """Tallentaa luetun kirjan tietokantaan."""
        cursor = self._connection.cursor()

        cursor.execute("""
                       INSERT INTO Books (date, title, author, pages, notes)
                       values (?, ?, ?, ?, ?)""",
                       (book.date, book.title, book.author, book.pages,
                        book.notes)
                       )

        self._connection.commit()

        return book

    def delete_all(self):
        """Poistaa kaikki tallennetut kirjat lukupäiävkirjasta."""
        cursor = self._connection.cursor()

        cursor.execute("DELETE From Books")

        self._connection.commit()

book_journal_repository = BookJournalRepository(get_database_connection())
