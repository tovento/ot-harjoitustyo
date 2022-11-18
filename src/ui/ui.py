from tkinter import ttk
from ui.book_journal_view import BookJournalView
from ui.add_read_book_view import AddReadBookView

class UI:
    """ TODO """

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_book_journal_view()
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self.current_view = None

    def _handle_book_journal_view(self):
        self._show_book_journal_view()

    def _show_book_journal_view(self):
        self._hide_current_view()

        self._current_view = BookJournalView(
                                self._root,
                                self._handle_add_read_book_view)
        self._current_view.pack()

    def _handle_add_read_book_view(self):
        self._show_add_read_book_view()

    def _show_add_read_book_view(self):
        self._hide_current_view()

        self._current_view = AddReadBookView(
                                self._root,
                                self._handle_book_journal_view)
        self._current_view.pack()
