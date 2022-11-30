from tkinter import ttk, constants
from services.book_journal_service import book_journal_service

class AddNoteToReadingList:
    """Näkymä, jossa käyttäjä voi lisätä muistiinpanon kirjasta, jonka haluaa
    lukea.
    """
    def __init__(self, root, handle_book_journal_view):
        """Luokan konstruktori. Luo uuden näkymän, jolla käyttäjä lisää kirjan
        lukulistalle.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_book_journal_view:
                Kutsuttava funktio, jolla siirrytään lukupäiväkirjan
                perusnäkymään.
        """
        self._root = root
        self._handle_book_journal_view = handle_book_journal_view
        self._frame = None

        self._initialize()

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
                            master=self._frame,
                            text="Lisää kirja lukulistalle")

        label = ttk.Label(master=self._frame, text="Kirja:")
        self._entry = ttk.Entry(master=self._frame)

        button = ttk.Button(
                    master=self._frame,
                    text="Lisää lukulistalle",
                    command=self._handle_adding_note)

        back_button = ttk.Button(
                     master=self._frame,
                     text="Takaisin",
                     command=self._handle_book_journal_view)

        heading_label.grid(padx=5, pady=5)
        label.grid(padx=5, pady=5)
        self._entry.grid(padx=5, pady=5)
        button.grid(padx=5, pady=5)
        back_button.grid(padx=5, pady=5)

    def _handle_adding_note(self):
        entry_value = self._entry.get()

        if entry_value:
            book_journal_service.add_readinglist_note(entry_value)

            self._handle_book_journal_view()
        else:
            pass
