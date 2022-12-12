from tkinter import ttk, constants
from services.book_journal_service import book_journal_service

class AddReadBookView:
    """Näkymä, jossa käyttäjä voi lisätä tietoja lukemastaan kirjasta."""

    def __init__(self, root, handle_book_journal_view):
        """Luokan konstruktori. Luo uuden näkymän, jolla käyttäjä voi lisätä
        lukemansa kirjan lukupäiväkirjaan.

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
        self._frame.pack(pady=30, padx=30, fill="both", expand=True)
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Lisää luettu kirja:")

        date_label = ttk.Label(master=self._frame, text="Pvm:")
        self._date_entry = ttk.Entry(master=self._frame)
        title_label = ttk.Label(master=self._frame, text="Nimi:")
        self._title_entry = ttk.Entry(master=self._frame)
        author_label = ttk.Label(master=self._frame, text="Kirjailija:")
        self._author_entry = ttk.Entry(master=self._frame)
        pages_label = ttk.Label(master=self._frame, text="Sivuja:")
        self._pages_entry = ttk.Entry(master=self._frame)
        notes_label = ttk.Label(master=self._frame, text="Merkintöjä:")
        self._notes_entry = ttk.Entry(master=self._frame)

        button = ttk.Button(
                    master=self._frame,
                    text="Lisää kirja",
                    command=self._handle_adding_book)
        
        back_button = ttk.Button(
                     master=self._frame,
                     text="Takaisin",
                     command=self._handle_book_journal_view)
        
        heading_label.grid(padx=5, pady=5)
        date_label.grid(padx=5, pady=5)
        self._date_entry.grid(padx=5, pady=5)
        title_label.grid(padx=5, pady=5)
        self._title_entry.grid(padx=5, pady=5)
        author_label.grid(padx=5, pady=5)
        self._author_entry.grid(padx=5, pady=5)
        pages_label.grid(padx=5, pady=5)
        self._pages_entry.grid(padx=5, pady=5)
        notes_label.grid(padx=5, pady=5)
        self._notes_entry.grid(padx=5, pady=5)

        button.grid(padx=5, pady=5)
        back_button.grid(padx=5, pady=5)

    def _handle_adding_book(self):
        date_value = self._date_entry.get()
        title_value = self._title_entry.get()
        author_value = self._author_entry.get()
        pages_value = self._pages_entry.get()
        notes_value = self._notes_entry.get()

        if date_value and title_value and author_value and pages_value:
            book_journal_service.add_read_book(
                                    date_value,
                                    title_value,
                                    author_value,
                                    pages_value,
                                    notes_value)

            self._handle_book_journal_view()
        else:
            pass
