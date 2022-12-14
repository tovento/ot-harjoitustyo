from entities.book_to_read import BookToRead
from database_connection import get_database_connection

class ReadingListRepository:
    """Lukulistan tietokantatoiminnoista vastaava luokka."""
    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio.
        """
        self._connection = connection

    def find_all_notes(self):
        """Hakee kaikki lukulistalle tallennetut muistiinpanot."""
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM BooksToRead")

        rows = cursor.fetchall()

        return [BookToRead(row["description"], row["id"]) for row in rows]

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

reading_list_repository = ReadingListRepository(get_database_connection())
