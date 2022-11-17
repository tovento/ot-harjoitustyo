from tkinter import ttk

class UI:
    """ TODO """

    def __init__(self, root):
        self._root = root

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Lukupäiväkirja")

        button = ttk.Button(master=self._root, text="Lisää luettu kirja")

        label = ttk.Label(master=self._root, text="Luetut kirjat:")

        heading_label.grid(padx=5, pady=5)
        button.grid(padx=5, pady=5)
        label.grid(padx=5, pady=5)
