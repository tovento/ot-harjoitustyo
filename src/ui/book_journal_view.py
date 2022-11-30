from tkinter import ttk
from services.book_journal_service import book_journal_service

class BookJournalView:
    """Lukupäiväkirjan perusnäkymä, jossa on kaksi välilehteä. Ensimmäisellä välilehdellä
    käyttäjä näkee lukemansa kirjat. Toisella välilehdellä on lukulista eli
    kirjat, jotka käyttäjä on merkinnyt haluavansa lukea.
    """

    def __init__(self, root, handle_add_read_book_view):
        """Luokan konstruktori. Luo lukupäiväkirjan perusnäkymän kahdella
        välilehdellä.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_add_read_book_view:
                Kutsuttava funktio, joka vie käyttäjän lomakkeeseen, jolla hän
                voi lisätä uuden luetun kirjan lukupäiväkirjaan.
        """

        self._root = root
        self._handle_add_read_book_view = handle_add_read_book_view
        self._frame1 = None
        self._frame2 = None
        self._notebook = ttk.Notebook(self._root)
        self._notebook.pack(pady=5, expand=True)

        self._initialize()

    def destroy(self):
        """Tuhoaa näkymät."""
        self._frame1.destroy()
        self._frame2.destroy()

    def pack(self):
        """Näyttää näkymät."""
        self._frame1.pack(fill="both", expand=True)
        self._frame2.pack(fill="both", expand=True)

        self._notebook.add(self._frame1, text="Lukupäiväkirja")
        self._notebook.add(self._frame2, text="Lukulista")
    
    def _initialize(self):
        self._frame1 = ttk.Frame(self._notebook)
        self._frame2 = ttk.Frame(self._notebook)

        heading_label1 = ttk.Label(master=self._frame1, text="Lukupäiväkirja")

        button1 = ttk.Button(
                    master=self._frame1,
                    text="Lisää luettu kirja",
                    command=self._handle_add_read_book_view)

        label1 = ttk.Label(master=self._frame1, text="Luetut kirjat:")
        books = book_journal_service.find_all_books()
        book_messages = [f"{book.date}: {book.author}: " \
                        f"{book.title}, {book.pages} sivua.\n " \
                        f"Muistiinpanot: {book.notes}"
                        for book in books]

        heading_label1.grid(padx=5, pady=5)
        button1.grid(padx=5, pady=5)
        label1.grid(padx=5, pady=5)

        for message in reversed(book_messages):
            book_list = ttk.Label(master=self._frame1, text=message)
            book_list.grid(padx=5, pady=5)

        heading_label2 = ttk.Label(master=self._frame2, text="Lukulista")

        button2 = ttk.Button(
                    master=self._frame2,
                    text="Lisää kirja lukulistalle")

        label2 = ttk.Label(master=self._frame2, text="Lukulista:")

        heading_label2.grid(padx=5, pady=5)
        button2.grid(padx=5, pady=5)
        label2.grid(padx=5, pady=5)
