from entities.book import Book
from entities.book_to_read import BookToRead
from database_connection import get_database_connection

class BookJournalRepository:
    """Tietokantatoiminnoista vastaava luokka."""
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
        """Poistaa kaikki tallennetut kirjat lukupäiväkirjasta ja
        lukulistalta.
        """
        cursor = self._connection.cursor()

        cursor.execute("DELETE From Books")
        cursor.execute("DELETE From BooksToRead")

        self._connection.commit()

    def find_all_notes(self):
        """Hakee kaikki lukulistalle tallennetut muistiinpanot."""
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM BooksToRead")

        rows = cursor.fetchall()

        return [(BookToRead(row["description"]), row["id"]) for row in rows]

    def save_note(self, note):
        """Tallentaa muistiinpanon lukulistalle."""
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO BooksToRead (description) values (?)",
                       (note.description,))

        self._connection.commit()

        return note

    def delete_note(self, note_id):
        """Poistaa yksittäisen muistiinpanon lukulistalta."""
        cursor= self._connection.cursor()
        cursor.execute("DELETE FROM BooksToRead WHERE id=(?)", (note_id,))

        self._connection.commit()

book_journal_repository = BookJournalRepository(get_database_connection())
