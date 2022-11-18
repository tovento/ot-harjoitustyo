from tkinter import ttk, constants

class AddReadBookView:
    """Näkymä, jossa käyttäjä voi lisätä titoja lukemastaan kirjasta."""

    def __init__(self, root, handle_book_journal_view):
        """TODO"""
        self._root = root
        self._handle_book_journal_view = handle_book_journal_view
        self._frame = None

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Lisää luettu kirja:")

        date_label = ttk.Label(master=self._frame, text="Pvm:")
        date_entry = ttk.Entry(master=self._frame)
        button = ttk.Button(
                    master=self._frame,
                    text="Lisää kirja")
        
        back_button = ttk.Button(
                     master=self._frame,
                     text="Takaisin",
                     command=self._handle_book_journal_view)
        
        heading_label.grid(padx=5, pady=5)
        date_label.grid(padx=5, pady=5)
        date_entry.grid(padx=5, pady=5)
        button.grid(padx=5, pady=5)
        back_button.grid(padx=5, pady=5)
