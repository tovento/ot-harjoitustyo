from entities.book import Book
from database_connection import get_database_connection

class BookJournalRepository:
    """Lukupäiväkirjan tietokantatoiminnoista vastaava luokka."""
    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio.
        """
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
                    row["notes"],
                    row["id"]) for row in rows]

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
        """Poistaa kaikki tallennetut kirjat lukupäiväkirjasta ja
        lukulistalta.
        """
        cursor = self._connection.cursor()

        cursor.execute("DELETE From Books")
        cursor.execute("DELETE From BooksToRead")

        self._connection.commit()

book_journal_repository = BookJournalRepository(get_database_connection())
