class Book:
    """Luettua kirjaa kuvaava olio.

    Attributes:
        date:
            Merkkijonoarvo, joka kuvaa päivämäärää, jolloin käyttäjä on lukenut
            kirjan loppuun.
        title: Merkkijonoarvo, joka kuvaa kirjan nimeä.
        author: Merkkijonoarvo, joka kuvaa kirjailijan nimeä.
        pages: Kokonaisluku, joka kuvaa kirjan sivujen määrää.
        notes: Merkkijonoarvo, joka kuvaa käyttäjän muistiinpanoja kirjasta.
        id: Kokonaisluku, olion tunnus tietokannassa.
    """

    def __init__(self, date, title, author, pages, notes=None, id=None):
        """Luokan konstruktori, joka luo uuden Book-olion.

        Args:
            date:
                Merkkijonoarvo, joka kuvaa päivämäärää, jolloin käyttäjä on
                lukenut kirjan loppuun.
            title: Merkkijonoarvo, joka kuvaa kirjan nimeä.
            author: Merkkijonoarvo, joka kuvaa kirjailijan nimeä.
            pages: Kokonaisluku, joka kuvaa kirjan sivujen määrää.
            notes:
                Vapaaehtoinen, oletustarvoltaan None.
                Merkkijonoarvo, joka kuvaa käyttäjän muistiinpanoja kirjasta.
            id:
                Oletusarvoltaan None. Kokonaisluku, jota käytetään
                tietokantaoperaatioiden yhteydessä.
        """
        self.date = date
        self.title = title
        self.author = author
        self.pages = pages
        self.notes = notes
        self.id = id
