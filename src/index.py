from tkinter import Tk
from ui.ui import UI
from initialize_database import initialize_database

def main():
    """Metodi, joka käynnistää sovelluksen. Alustaa ensin tietokannan ja käynnistää sen
    jälkeen käyttöliittymän.
    """
    initialize_database()

    window = Tk()
    window.title("Lukupäiväkirja")
    window.minsize(300, 300)
    window['background'] = '#dfd5e1'

    user_interface = UI(window)
    user_interface.start()

    window.mainloop()

if __name__ == "__main__":
    main()
