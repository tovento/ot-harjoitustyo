class BookToRead:
    """Luettavaa kirjaa kuvaava olio.

    Attributes:
        description: 
            Merkkijonoarvo. Kuvaa kirjaa, jonka käyttäjä haluaa lukea.
            Voi olla esim. kirjan tai kirjailijan nimi, tyyli käyttäjän
            vapaasti valittavissa.
    """

    def __init__(self, description):
        """Luokan konstruktori, joka luo uuden BookToRead-olion.

        Args:
            description: Merkkijonoarvo, joka kuvaa kirjaa, jonka käyttäjä
            haluaa lukea. Voi olla esim. kirjan tai kirjailijan nimi.
        """
        self.description = description
