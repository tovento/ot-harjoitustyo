from tkinter import ttk, constants
from services.book_journal_service import book_journal_service
from services.reading_list_service import reading_list_service

class BookJournalView:
    """Lukupäiväkirjan perusnäkymä, jossa on kaksi välilehteä. Ensimmäisellä välilehdellä
    käyttäjä näkee lukemansa kirjat. Toisella välilehdellä on lukulista eli
    kirjat, jotka käyttäjä on merkinnyt haluavansa lukea.
    """

    def __init__(self,
                 root,
                 handle_book_journal_view,
                 handle_add_read_book_view,
                 handle_add_note_to_reading_list_view):
        """Luokan konstruktori. Luo lukupäiväkirjan perusnäkymän kahdella
        välilehdellä.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_book_journal_view:
                Kutsuttava funktio, joka alustaa Lukupäiväkirjan näkymät
                uudelleen.
            handle_add_read_book_view:
                Kutsuttava funktio, joka vie käyttäjän lomakkeeseen, jolla hän
                voi lisätä uuden luetun kirjan lukupäiväkirjaan.
            handle_add_note_to_reading_list_view:
                Kutsuttava funktio, joka vie käyttäjän lomakkeeseen, jolla hän
                voi lisätä muistiinpanon lukulistalle.
        """

        self._root = root
        self._handle_view = handle_book_journal_view
        self._handle_add_book = handle_add_read_book_view
        self._handle_add_note = handle_add_note_to_reading_list_view
        self._frame1 = None
        self._frame2 = None
        self._notebook = ttk.Notebook(self._root)
        self._notebook.pack(pady=30, padx=30, fill="both", expand=True)

        self._initialize()

    def destroy(self):
        """Tuhoaa näkymät."""
        self._notebook.destroy()

    def pack(self):
        """Näyttää näkymät."""
        self._frame1.pack(fill="both", expand=True)
        self._frame2.pack(fill="both", expand=True)

        self._notebook.add(self._frame1, text="Lukupäiväkirja")
        self._notebook.add(self._frame2, text="Lukulista")
    
    def _initialize(self):
        self._frame1 = ttk.Frame(self._notebook)
        self._frame2 = ttk.Frame(self._notebook)

        self._initialize_bookjournal_frame(self._frame1)
        self._initialize_readinglist_frame(self._frame2)

    def _initialize_bookjournal_frame(self, frame):

        heading_label1 = ttk.Label(master=frame, text="Lukupäiväkirja")

        button1 = ttk.Button(
                    master=frame,
                    text="Lisää luettu kirja",
                    command=self._handle_add_book)

        label1 = ttk.Label(master=frame, text="Luetut kirjat:")
        books = book_journal_service.find_all_books()
        book_messages = [f"{book.date}: {book.author}: " \
                        f"{book.title}, {book.pages} sivua.\n " \
                        f"Muistiinpanot: {book.notes}"
                        for book in books]

        heading_label1.grid(padx=5, pady=5)
        button1.grid(padx=5, pady=5)
        label1.grid(padx=5, pady=5)

        for message in reversed(book_messages):
            book_list = ttk.Label(master=frame, text=message)
            book_list.grid(padx=5, pady=5)

    def _initialize_readinglist_frame(self, frame):
        heading_label2 = ttk.Label(master=frame, text="Lukulista")

        button2 = ttk.Button(
                    master=frame,
                    text="Lisää kirja lukulistalle",
                    command=self._handle_add_note)

        label2 = ttk.Label(master=frame, text="Lukulista:")

        notes = reading_list_service.find_all_notes()

        heading_label2.grid(padx=5, pady=5)
        button2.grid(padx=5, pady=5)
        label2.grid(padx=5, pady=5)

        for note in notes:
            self._initialize_notes(frame, note)

    def _initialize_notes(self, frame, note):
        note_frame = ttk.Frame(master=frame)
        label = ttk.Label(master=note_frame, text=note.description)

        delete_button = ttk.Button(
                            master=note_frame,
                            text="Poista",
                            command=lambda: self._handle_delete_note(note.id))

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)
        delete_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)

        note_frame.grid_columnconfigure(0, weight=1)
        note_frame.grid()

    def _handle_delete_note(self, note_id):
        reading_list_service.delete_note(note_id)
        self._handle_view()
