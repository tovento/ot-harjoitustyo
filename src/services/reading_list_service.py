from entities.book_to_read import BookToRead
from repositories.reading_list_repository import reading_list_repository as rlr

class ReadingListService:
    """Lukupäiväkirjan sovelluslogiikasta vastaava luokka."""

    def __init__(self, reading_list_repository=rlr):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan
        palvelun.

        Args:
            reading_list_repository:
                ReadingListRepository-olio.
        """
        self._reading_list_repository = reading_list_repository

    def add_readinglist_note(self, description):
        """Lisää muistiinpanon lukulistalle."""
        note = BookToRead(description)

        self._reading_list_repository.save_note(note)

        return note

    def find_all_notes(self):
        """Hakee listan lukulistaan tallennetuista muistiinpanoista."""
        notes = self._reading_list_repository.find_all_notes()

        return notes

    def delete_note(self, note_id):
        """Poistaa yksittäisen muistiinpanon lukulistalta."""
        self._reading_list_repository.delete_note(note_id)

reading_list_service = ReadingListService()
