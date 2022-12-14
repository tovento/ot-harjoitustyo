class BookToRead:
    """Luettavaa kirjaa kuvaava olio.

    Attributes:
        description:
            Merkkijonoarvo. Kuvaa kirjaa, jonka käyttäjä haluaa lukea.
            Voi olla esim. kirjan tai kirjailijan nimi, tyyli käyttäjän
            vapaasti valittavissa.
        id: Kokonaisluku, olion tunnus tietokannassa.
    """

    def __init__(self, description, id=None):
        """Luokan konstruktori, joka luo uuden BookToRead-olion.

        Args:
            description:
                Merkkijonoarvo, joka kuvaa kirjaa, jonka käyttäjä
                haluaa lukea. Voi olla esim. kirjan tai kirjailijan nimi.
            id:
                Oletusarvoltaan None. Kokonaisluku, jota käytetään
                tietokantaoperaatioiden yhteydessä.
        """
        self.description = description
        self.id = id
