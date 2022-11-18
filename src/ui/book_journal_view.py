from tkinter import ttk, constants

class BookJournalView:
    """Näkymä, jossa listataan luetut kirjat."""

    def __init__(self, root, handle_add_read_book_view):
        """TODO"""

        self._root = root
        self._handle_add_read_book_view = handle_add_read_book_view
        self._frame = None

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Lukupäiväkirja")

        button = ttk.Button(
                    master=self._frame,
                    text="Lisää luettu kirja",
                    command=self._handle_add_read_book_view)

        label = ttk.Label(master=self._frame, text="Luetut kirjat:")

        heading_label.grid(padx=5, pady=5)
        button.grid(padx=5, pady=5)
        label.grid(padx=5, pady=5)
